
<body>

<h1>Projeto: Estação Meteorológica com Django e ESP32</h1> <!-- tag de titulo-->

<p>Este projeto é uma estação meteorológica completa que coleta dados ambientais (como temperatura, umidade, pressão atmosférica e luminosidade) através de sensores conectados a uma ESP32. Os dados são enviados a um servidor Django, que armazena e exibe as informações em um dashboard com gráficos e relatórios detalhados.</p>

<h2>Índice</h2> <!--tag de subtitulo -->
<ul>  <!--tag de  lista -->
  <li><a href="#objetivo">Objetivo</a></li>
  <li><a href="#arquitetura-do-projeto">Arquitetura do Projeto</a></li>
  <li><a href="#pré-requisitos">Pré-requisitos</a></li>
  <li><a href="#configuração-do-projeto">Configuração do Projeto</a></li>
  <li><a href="#estrutura-de-arquivos">Estrutura de Arquivos</a></li>
  <li><a href="#uso">Uso</a></li>
  <li><a href="#funcionalidades">Funcionalidades</a></li>
  <li><a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
  <li><a href="#próximas-implementações">Próximas Implementações</a></li>
  <li><a href="#contribuição">Contribuição</a></li>
  <li><a href="#licença">Licença</a></li>
</ul>

<h2 id="objetivo">Objetivo</h2>
<p>Desenvolver uma estação meteorológica em tempo real para monitorar e registrar dados climáticos, com fácil acesso e visualização. Este sistema é ideal para propriedades rurais ou locais onde é importante monitorar as condições ambientais de forma remota e centralizada.</p>

<h2 id="arquitetura-do-projeto">Arquitetura do Projeto</h2>
<ol>
  <li><strong>ESP32</strong>: Captura dados dos sensores (DHT22, BMP180, LDR/MH-RD) e envia-os ao servidor Django através de requisições HTTP.</li>
  <li><strong>Django (Servidor)</strong>: Recebe os dados, armazena no banco de dados e disponibiliza visualização em um dashboard web.</li>
  <li><strong>Frontend</strong>: Exibe gráficos e relatórios dos dados coletados, além de fornecer alertas sobre condições específicas (como níveis de luz ou temperatura fora do padrão).</li>
</ol>

<h2 id="pré-requisitos">Pré-requisitos</h2>
<ul>
  <li><strong>Hardware</strong>:
    <ul>
      <li>ESP32</li>
      <li>Sensor de temperatura e umidade (DHT22)</li>
      <li>Sensor de pressão atmosférica (BMP180)</li>
      <li>Sensor de luminosidade (LDR/MH-RD)</li>
    </ul>
  </li>
  <li><strong>Software</strong>:
    <ul>
      <li>Python 3.8+</li>
      <li>Django 4.0+</li>
      <li>Bibliotecas de sensores para a ESP32 (usadas com Arduino IDE)</li>
      <li>Biblioteca Django Rest Framework para API</li>
    </ul>
  </li>
</ul>

<h2 id="configuração-do-projeto">Configuração do Projeto</h2>

<h3>1. Configuração do Servidor Django</h3>
<ol>
  <li><strong>Clone este repositório</strong>:
    <pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
    </code></pre>
  </li>

  <li><strong>Instale as dependências</strong>:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li><strong>Configuração do Banco de Dados</strong>: Configure o banco de dados em <code>settings.py</code> (usando SQLite para testes locais ou PostgreSQL para produção).</li>

  <li><strong>Migre os modelos para o banco de dados</strong>:
    <pre><code>python manage.py migrate</code></pre>
  </li>

  <li><strong>Crie um superusuário para acessar o Django Admin</strong>:
    <pre><code>python manage.py createsuperuser</code></pre>
  </li>

  <li><strong>Inicie o servidor Django</strong>:
    <pre><code>python manage.py runserver</code></pre>
  </li>
</ol>

<h3>2. Configuração da ESP32</h3>
<ol>
  <li>Instale a Arduino IDE e as bibliotecas para os sensores usados.</li>
  <li>Configure a ESP32 com o código na pasta <code>ESP32_Code</code>.</li>
  <li>Altere as configurações de Wi-Fi e URL do servidor no código da ESP32 para apontar para o servidor Django.</li>
</ol>

<h2 id="estrutura-de-arquivos">Estrutura de Arquivos</h2>
<pre><code>.
├── ESP32_Code                # Código-fonte para a ESP32 (Arduino IDE)
├── my_project                # Pasta do projeto Django
│   ├── sensors               # App Django para sensores
│   ├── templates             # Templates HTML para o dashboard
│   └── ...                   # Outros arquivos do projeto
├── requirements.txt          # Dependências do Django
└── README.md                 # Este README
</code></pre>

<h2 id="uso">Uso</h2>
<ol>
  <li><strong>Inicie o servidor Django</strong> e acesse o dashboard em <code>http://127.0.0.1:8000</code>.</li>
  <li><strong>Conecte a ESP32</strong> à mesma rede Wi-Fi do servidor e verifique se os dados estão sendo enviados corretamente.</li>
  <li><strong>Monitore os dados</strong> em tempo real pelo dashboard.</li>
</ol>

<h2 id="funcionalidades">Funcionalidades</h2>
<ul>
  <li><strong>Coleta de Dados</strong>: Recebe dados de temperatura, umidade, pressão e luminosidade da ESP32.</li>
  <li><strong>Armazenamento de Dados</strong>: Salva os dados em um banco de dados para consultas futuras.</li>
  <li><strong>Dashboard Interativo</strong>: Exibe gráficos e relatórios dos dados coletados.</li>
  <li><strong>Alertas</strong>: Notificações sobre condições críticas (em desenvolvimento).</li>
  <li><strong>API</strong>: Endpoints para receber dados dos sensores.</li>
</ul>

<h2 id="tecnologias-utilizadas">Tecnologias Utilizadas</h2>
<ul>
  <li><strong>Backend</strong>: Django, Django Rest Framework</li>
  <li><strong>Frontend</strong>: HTML, CSS, JavaScript (para gráficos e visualizações)</li>
  <li><strong>Microcontrolador</strong>: ESP32, sensores (DHT22, BMP180, LDR/MH-RD)</li>
  <li><strong>Banco de Dados</strong>: SQLite (para desenvolvimento) ou PostgreSQL</li>
</ul>

<h2 id="próximas-implementações">Próximas Implementações</h2>
<ul>
  <li>[ ] Envio de alertas por e-mail ou SMS</li>
  <li>[ ] Visualização histórica de dados em diferentes intervalos de tempo</li>
  <li>[ ] Integração com modelos de previsão do tempo</li>
  <li>[ ] Interface para configurar novos sensores</li>
</ul>

<h2 id="contribuição">Contribuição</h2>
<p>Sinta-se à vontade para contribuir! Por favor, envie um pull request ou abra uma issue para sugestões de melhorias ou novas funcionalidades.</p>

<h2 id="licença">Licença</h2>
<p>Este projeto é licenciado sob a <a href="LICENSE">MIT License</a>.</p>

</body>
</html>
