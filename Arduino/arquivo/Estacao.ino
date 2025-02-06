#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <DHT.h>
#include <DHT_U.h>

// Pinos dos sensores
#define DHTPIN 26           // Pino do sensor DHT
#define DHTTYPE DHT22       // Tipo de sensor DHT
#define ANEMOMETER_PIN 25   // Anemômetro
#define RAIN_SENSOR_PIN 32  // Pluviômetro
#define WIND_DIR_PIN_N 14   // Biruta sensor 1
#define WIND_DIR_PIN_L 12   // Biruta sensor 2
#define WIND_DIR_PIN_O 13   // Biruta sensor 3
#define WIND_DIR_PIN_S 27   // Biruta sensor 4
#define SDA_PIN 21          // Define pino 21 SDA 
#define SCL_PIN 22          // Define pino 22 SCL

// Configuração WiFi
const char* ssid = "vigilantes";
const char* password = "vigilantes2024";
const String serverURL = "https://project-estacao.vercel.app/sensors/";
const String authKey = "a3333637da4fb60f43dac187f305d649cac80f66";

// Sensores
DHT dht(DHTPIN, DHTTYPE);
Adafruit_BMP280 bmp;

// Variáveis globais
volatile int anemometerPulses = 0;
volatile int rainPulses = 0;
// calibração anemometro
float fatorcalibracao = 2.5;

// Funções de interrupção
void IRAM_ATTR countRainPulse() { rainPulses++; }

// Conexão WiFi
void configurarWiFi() {
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Conectando ao WiFi...");
    }
    Serial.println("Conectado ao WiFi!");
}

// Inicializar componentes
void inicializarComponentes() {
    dht.begin();
    Wire.begin(SDA_PIN, SCL_PIN);
    if (!bmp.begin(0x76)) {
        Serial.println("Erro ao inicializar o sensor BMP280!");
    } else {
        Serial.println("BMP280 inicializado com sucesso.");
    }

    pinMode(ANEMOMETER_PIN, INPUT_PULLUP);
    pinMode(RAIN_SENSOR_PIN, INPUT_PULLUP);
    pinMode(WIND_DIR_PIN_N, INPUT_PULLUP);
    pinMode(WIND_DIR_PIN_L, INPUT_PULLUP);
    pinMode(WIND_DIR_PIN_O, INPUT_PULLUP);
    pinMode(WIND_DIR_PIN_S, INPUT_PULLUP);

    // attachInterrupt(digitalPinToInterrupt(ANEMOMETER_PIN), countAnemometerPulse, RISING); // Server para contar os pulsos do anemômetro
    attachInterrupt(digitalPinToInterrupt(RAIN_SENSOR_PIN), countRainPulse, RISING);
}

// Coleta de dados brutos
void coletarDados(float &temperatura_dht, float &umidade, float &temperatura_bmp, float &pressao_bmp, unsigned int &anemometro, unsigned int &pluviometro, String &direcao_vento) {
    // Leitura de sensores de temperatura, umidade e pressão
    temperatura_dht = dht.readTemperature();   // Temperatura do DHT
    umidade = dht.readHumidity();              // Umidade do DHT
    temperatura_bmp = bmp.readTemperature();   // Temperatura do BMP280
    pressao_bmp = bmp.readPressure() / 100;    // Pressão do BMP280 em hPa

    // Contagem de pulsos do anemômetro
    anemometro = (anemometerPulses * fatorcalibracao);

    // Contagem de pulsos do pluviômetro
    pluviometro = rainPulses;

    // Determinar direção do vento com base nos sensores da biruta
    if (digitalRead(WIND_DIR_PIN_N) == HIGH) {
        direcao_vento = "N";
    } else if (digitalRead(WIND_DIR_PIN_L) == HIGH) {
        direcao_vento = "L";
    } else if (digitalRead(WIND_DIR_PIN_O) == HIGH) {
        direcao_vento = "O";
    } else if (digitalRead(WIND_DIR_PIN_S) == HIGH) {
        direcao_vento = "S";
    } else {
        direcao_vento = "Indefinido"; // Caso nenhum sensor seja ativado
    }
}


// Envio de dados ao Django
void enviarDados(float temperatura_dht, float umidade, float temperatura_bmp, float pressao_bmp, float anemometro, unsigned int pluviometro, bool sensor_vento_N, bool sensor_vento_L, bool sensor_vento_O, bool sensor_vento_S) {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin(serverURL);
        http.addHeader("Content-Type", "application/json");
        http.addHeader("Authorization", authKey);

        // Formata o JSON
        String jsonData = "{";
        jsonData += "\"temperatura_dht\": " + String(temperatura_dht) + ",";
        jsonData += "\"umidade\": " + String(umidade) + ",";
        jsonData += "\"temperatura_bmp\": " + String(temperatura_bmp) + ",";
        jsonData += "\"pressao_bmp\": " + String(pressao_bmp) + ",";
        jsonData += "\"anemometro\": " + String(anemometro) + ",";
        jsonData += "\"pluviometro\": " + String(pluviometro) + ",";
        // Biruta
        if (sensor_vento_N) {
            jsonData += "\"biruta\": \"N\"";
        } else if (sensor_vento_L) {
            jsonData += "\"biruta\": \"L\"";
        } else if (sensor_vento_O) {
            jsonData += "\"biruta\": \"O\"";
        } else {
            jsonData += "\"biruta\": \"S\"";
        }
        jsonData += "}";

        // Envia os dados
        int httpResponseCode = http.POST(jsonData);
        if (httpResponseCode > 0) {
            String response = http.getString();
            Serial.println("Dados enviados com sucesso: " + response);
        } else {
            Serial.println("Erro ao enviar dados: " + String(httpResponseCode));
        }
        http.end();
    } else {
        Serial.println("Não conectado ao WiFi.");
    }
}

// Modo de sono profundo
void entrarEmSonoProfundo() {
    Serial.println("Entrando em modo de sono profundo.");
    esp_sleep_enable_timer_wakeup(900000); // 15 minutos
    esp_deep_sleep_start();
}

// Função principal
void setup() {
    Serial.begin(115200);
    configurarWiFi();
    inicializarComponentes();
}

void loop() {
    float temperatura_dht, umidade, temperatura_bmp, pressao_bmp;
    unsigned int anemometro, pluviometro;
    bool sensor_vento_N, sensor_vento_L, sensor_vento_O, sensor_vento_S;

    // Coleta dos dados
    coletarDados(temperatura_dht, umidade, temperatura_bmp, pressao_bmp, anemometro, pluviometro, sensor_vento_N, sensor_vento_L, sensor_vento_O, sensor_vento_S);
    // Adiciona um pequeno delay para estabilizar a leitura dos sensores
    delay(15000);  // Delay de 15 segundos para garantir precisão na leitura dos sensores

    // Envia para o servidor
    enviarDados(temperatura_dht, umidade, temperatura_bmp, pressao_bmp, anemometro, pluviometro, sensor_vento_N, sensor_vento_L, sensor_vento_O, sensor_vento_S);

    // Reseta os pulsos para a próxima leitura
    rainPulses = 0;

    entrarEmSonoProfundo();
}
