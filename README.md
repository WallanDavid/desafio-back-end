# Projeto de Integração de Sistemas para Análise de Densidade de Chuva

Este projeto visa desenvolver uma aplicação que integra-se à plataforma colaborativa de cadastro de dispositivos IoT para fornecer insights para tomada de decisão de plantio na indústria agrária. A aplicação utiliza os equipamentos da PredictWeather para medir a densidade de chuva.

## Funcionalidades Principais

- Autenticação de Usuários: Os usuários devem poder autenticar-se na aplicação para consultar os dados de volumetria de chuva.
- Filtragem de Dispositivos: Apenas dispositivos cujo fabricante seja a PredictWeather e que possuam o comando `get_rainfall_intensity` são considerados pela aplicação.
- Consulta de Dispositivos: A aplicação tem um endpoint que retorna uma lista dos dispositivos cadastrados na API que atendem aos requisitos de filtragem.
- Obtenção de Medições de Chuva: Para cada dispositivo na lista, a aplicação se conecta ao dispositivo via Telnet e envia o comando apropriado para receber as medições de chuva.
- Inclusão de Dados de Medições: Os dados das medições de chuva são incluídos na mensagem de resposta do endpoint de consulta de dispositivos.
- Otimização de Requisições: A aplicação aplica métodos para otimizar as requisições e reduzir o tempo de resposta, como o uso de multiprocessamento.

## Tecnologias Utilizadas

- Python: Linguagem de programação utilizada para desenvolver a aplicação.
- Flask: Framework web utilizado para criar a aplicação e seus endpoints.
- Telnetlib: Biblioteca Python utilizada para se conectar aos dispositivos via Telnet.
- Requests: Biblioteca Python utilizada para fazer requisições HTTP à API de cadastro de dispositivos IoT.

## Instalação

1. Clone este repositório: 


2. Instale as dependências: pip install -r requirements.txt


3. Execute a aplicação: python run.py


## Uso

- Acesse os endpoints da aplicação utilizando um cliente HTTP ou faça requisições via cURL para interagir com as funcionalidades.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para relatar bugs, sugerir melhorias ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
