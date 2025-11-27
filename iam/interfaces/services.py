from flask import Blueprint, request, jsonify

from iam.application.services import AuthApplicationService

iam_api = Blueprint('iam_api', __name__)
auth_service = AuthApplicationService()

# Device Repository
# Handle devices
@iam_api.route('/api/v1/devices/insert_device', methods=['POST'])
def insert_device():
    data = request.get_json()
    device_id = data.get('device_id')
    api_key = data.get('api_key')

    if not device_id or not api_key:
        return jsonify({'error': 'Missing device_id or api_key'}), 400

    auth_service.device_repository.insert_device(device_id, api_key) 
    
    return jsonify({'message': 'Device inserted successfully'}), 201

def authenticate_request():
    
    device_id = request.get_json().get('device_id')
    api_key = request.headers.get('X-API-KEY')

    if not device_id or not api_key:
        return jsonify({'error': 'Missing device_id or API key'}), 401
    if not auth_service.authenticate_device(device_id, api_key):
        return jsonify({'error': 'Authentication failed'}), 403
    return None