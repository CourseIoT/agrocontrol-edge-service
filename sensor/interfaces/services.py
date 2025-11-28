from datetime import datetime, timezone
from flask import Blueprint, request, jsonify

from sensor.application.services import SensorRecordApplicationService
from iam.interfaces.services import authenticate_request

sensor_api = Blueprint('sensor_api', __name__)
sensor_record_service = SensorRecordApplicationService()

@sensor_api.route('/api/v1/sensors/sensor-records', methods=['POST'])
def create_sensor_record():

    auth_result = authenticate_request()
    if auth_result:
        return auth_result
    
    data = request.get_json()
    print(f"fff {data}")

    try:
        device_id = data.get('device_id')
        api_key = request.headers.get('X-API-KEY')
        
        airHumidity = data.get('air_humidity')
        airTemperature = data.get('temperature') 

        soilMoisture1 = data.get('soil_1')
        soilMoisture2 = data.get('soil_2')
        soilMoisture3 = data.get('soil_3')
        avgSoilMoisture = data.get('soil_average') 
        pumpState = data.get('pump_active')           
        
        if api_key is None:
            return jsonify({'error': 'Missing API key in headers'}), 401
        
        if device_id is None: 
            return jsonify({'error': 'Missing device_id in request body'}), 400
        
        required_fields = [airHumidity, airTemperature, avgSoilMoisture, pumpState]
        
        if any(field is None for field in required_fields):
            return jsonify({'error': 'Missing some sensor data (check temperature, humidity, soil or pump fields)'}), 400

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
        return jsonify({'error': str(ve)}), 400
    
@sensor_api.route('/api/v1/sensors/enable-water-pump', methods=['POST'])
def enable_water_pump():
    auth_result = authenticate_request()
    if auth_result:
        return auth_result
    
    device_id = request.args.get('device_id')
    api_key = request.headers.get('X-API-KEY')

    if api_key is None:
        return jsonify({'error': 'Missing API key in headers'}), 401
    
    if device_id is None:
        return jsonify({'error': 'Missing device_id in query parameters'}), 400

    try:
        sensor_record_service.enable_water_pump(device_id, api_key)
        return jsonify({'message': f'Water pump enabled for device {device_id}'}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400