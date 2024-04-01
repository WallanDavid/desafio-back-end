from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL da API de dispositivos IoT
API_URL = "http://exemplo.com/api/devices"

# Função para obter a lista de dispositivos filtrados
def get_filtered_devices():
    response = requests.get(API_URL)
    devices = response.json()
    filtered_devices = [device for device in devices if device['manufacturer'] == 'PredictWeather' and 'get_rainfall_intensity' in device['commands']]
    return filtered_devices

# Função para obter medições de chuva de um dispositivo via Telnet (simplificada para este exemplo)
def get_rainfall_measurement(device_ip, device_port):
    # Implemente a lógica para se conectar via Telnet e obter as medições de chuva
    measurement = "123 mm"  # Exemplo de medição de chuva
    return measurement

# Endpoint para listar dispositivos e suas medições de chuva
@app.route('/devices', methods=['GET'])
def get_devices_and_measurements():
    devices = get_filtered_devices()
    device_measurements = []
    for device in devices:
        measurement = get_rainfall_measurement(device['ip'], device['port'])
        device_measurements.append({
            'device_id': device['id'],
            'measurement': measurement
        })
    return jsonify(device_measurements)

if __name__ == '__main__':
    app.run(debug=True)
