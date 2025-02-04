int sensorPins[] = {34, 35, 32, 33}; // Pinos conectados aos sensores Hall
int sensorStates[4];

void setup() {
    Serial.begin(115200);
    for (int i = 0; i < 4; i++) {
        pinMode(sensorPins[i], INPUT_PULLUP);
    }
}

void loop() {
    for (int i = 0; i < 4; i++) {
        sensorStates[i] = digitalRead(sensorPins[i]);
    }

    direcao = determinarDirecao(sensorStates);
    Serial.print("Direção: ");
    Serial.println(direcao);

    delay(1000);
}

String determinarDirecao(int estados[]) {
    if (estados[0] == HIGH && estados[1] == LOW && estados[2] == LOW && estados[3] == LOW) {
        return "Norte";
    } else if (estados[0] == HIGH && estados[1] == HIGH && estados[2] == LOW && estados[3] == LOW) {
        return "Nordeste";
    } else if (estados[0] == LOW && estados[1] == HIGH && estados[2] == LOW && estados[3] == LOW) {
        return "Leste";
    } else if (estados[0] == LOW && estados[1] == HIGH && estados[2] == HIGH && estados[3] == LOW) {
        return "Sudeste";
    } else if (estados[0] == LOW && estados[1] == LOW && estados[2] == HIGH && estados[3] == LOW) {
        return "Sul";
    } else if (estados[0] == LOW && estados[1] == LOW && estados[2] == HIGH && estados[3] == HIGH) {
        return "Sudoeste";
    } else if (estados[0] == LOW && estados[1] == LOW && estados[2] == LOW && estados[3] == HIGH) {
        return "Oeste";
    } else if (estados[0] == HIGH && estados[1] == LOW && estados[2] == LOW && estados[3] == HIGH) {
        return "Noroeste";
    }
    // Adicione mais condições para as outras direções
    return "Desconhecida";
}
