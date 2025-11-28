from flask import Flask

from shared.infastructure.database import DatabaseInitializer
from iam.application.services import AuthApplicationService

from iam.interfaces.services import iam_api
from sensor.interfaces.services import sensor_api

app = Flask(__name__)
app.register_blueprint(iam_api)
app.register_blueprint(sensor_api)

def setup():

    # Initialize the database
    DatabaseInitializer().init_database()

    auth_application_service = AuthApplicationService()
    test_device = auth_application_service.get_or_create_test_device()

    if test_device:
        print(f"Tested device successfully with ID: {test_device.device_id} and API Key: {test_device.api_key}")
          
# Run the application
if __name__ == "__main__":
    setup()
    app.run(host="0.0.0.0", port=5000, debug=True)
