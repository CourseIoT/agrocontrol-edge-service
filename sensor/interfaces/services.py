from flask import Blueprint, request, jsonify
from datetime import datetime, timezone

from sensor.application.services import SensorRecordApplicationService
from iam.interfaces.services import authenticate_request

sensor_api = Blueprint('sensor_api', __name__)

sensor_record_service = SensorRecordApplicationService()

@sensor_api.route('/api/v1/sensor-records', methods=['POST'])
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
        
        now=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ");

        if api_key is None:
            return jsonify({'error': 'Missing API key in headers'}), 401
    
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
    except KeyError:
        return jsonify({'error': 'Missing required fields'}), 400
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 404
    