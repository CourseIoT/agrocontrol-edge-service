from datetime import datetime, timezone
from flask import Blueprint, request, jsonify

from sensor.application.services import SensorRecordApplicationService
from iam.interfaces.services import authenticate_request

sensor_api = Blueprint('sensor_api', __name__)
sensor_record_service = SensorRecordApplicationService()

@sensor_api.route('/api/v1/sensors/sensor-records', methods=['POST'])
def create_sensor_record():

    # 1. Autenticación global (Middleware o función helper)
    auth_result = authenticate_request()
    if auth_result:
        return auth_result
    
    data = request.get_json()
    print(f"fff {data}")

    try:
        # 2. Extracción de datos del Request
        device_id = data.get('device_id')
        api_key = request.headers.get('X-API-KEY')
        
        # Nuevas variables
        airHumidity = data.get('air_humidity')
        airTemperature = data.get('temperature') # Antes temperature

        soilMoisture1 = data.get('soil_1')
        soilMoisture2 = data.get('soil_2')
        soilMoisture3 = data.get('soil_3')
        avgSoilMoisture = data.get('soil_average') # Antes humidityFloor
        pumpState = data.get('pump_active')           # Antes bombWaterOk
        
        # Nota: levelWaterOk ha sido eliminado del sistema

        # 3. Validaciones básicas de presencia
        if api_key is None:
            return jsonify({'error': 'Missing API key in headers'}), 401
        
        if device_id is None: 
            return jsonify({'error': 'Missing device_id in request body'}), 400
        
        # Verificamos que no falte ningún dato del sensor
        required_fields = [airHumidity, airTemperature, avgSoilMoisture, pumpState]
        
        if any(field is None for field in required_fields):
            return jsonify({'error': 'Missing some sensor data (check temperature, humidity, soil or pump fields)'}), 400

        # Generar timestamp
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


        record = sensor_record_service.create_and_save_sensor_record(
            device_id=device_id, 
            api_key=api_key, 
            airHumidity=airHumidity,
            airTemperature=airTemperature,
            soilMoisture1=soilMoisture1,
            soilMoisture2=soilMoisture2,
            soilMoisture3=soilMoisture3,
            avgSoilMoisture=avgSoilMoisture,
            pumpState=pumpState,
            created_at=now
        )

        print(f"Sensor record created for device {record}")
        
        # 5. Respuesta Exitosa (201 Created)
        return jsonify({
            "device_id": record.device_id,
            "airHumidity": record.airHumidity,
            "airTemperature": record.airTemperature,
            "soilMoisture1": record.soilMoisture1,
            "soilMoisture2": record.soilMoisture2,
            "soilMoisture3": record.soilMoisture3,
            "avgSoilMoisture": record.avgSoilMoisture,
            "pumpState": record.pumpState,
            "created_at": now
        }), 201
    
    except ValueError as ve:
        # Errores de validación de negocio (rangos) o autenticación de dispositivo
        return jsonify({'error': str(ve)}), 400