from datetime import datetime, timezone

from flask import Blueprint, request, jsonify

from sensor.application.services import SensorRecordApplicationService
from iam.interfaces.services import authenticate_request

sensor_api = Blueprint('sensor_api', __name__)
sensor_record_service = SensorRecordApplicationService()

@sensor_api.route('/api/v1/sensors/sensor_records', methods=['POST'])
def create_sensor_record():

    auth_result = authenticate_request()
    if auth_result:
        return auth_result
    
    data = request.get_json()

    try:
        device_id = data.get('device_id')
        api_key = request.headers.get('X-API-KEY')
        temperature = data.get('temperature')
        humidityAir = data.get('humidityAir')
        humidityFloor = data.get('humidityFloor')
        levelWaterOk = data.get('levelWaterOk')
        bombWaterOk = data.get('bombWaterOk')

        if api_key is None:
            return jsonify({'error': 'Missing API key in headers'}), 401
        
        if device_id is None: 
            return jsonify({'error': 'Missing device_id in request body'}), 400
        
        if temperature is None or humidityAir is None or humidityFloor is None or levelWaterOk is None or bombWaterOk is None:
            return jsonify({'error': 'Missing some sensor data in request body'}), 400

        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ");
    
        record = sensor_record_service.create_and_save_sensor_record(
            device_id, api_key, temperature, humidityAir, humidityFloor, levelWaterOk, bombWaterOk, now)
        return jsonify({
            "device_id": record.device_id,
            "temperature": record.temperature,
            "humidityAir": record.humidityAir,
            "humidityFloor": record.humidityFloor,
            "levelWaterOk" : record.levelWaterOk,
            "bombWaterOk": record.bombWaterOk,
            "created_at": now}), 201
    
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 404
    