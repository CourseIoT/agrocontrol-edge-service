# AgroControl Edge Service


## API Endpoints
- `POST /api/v1/devices/insert_device`: Register a devices.
- `POST /api/v1/sensors/sensor-records`: Insert a sensor data.
- `POST /api/v1/sensors/enable-water-pump`: Enable water pump for a device.
## How to install

Create a virtual environment if doesn't exists.
```sh
python -m venv venv
```

### Linux:
Enter to the virtual environment. 
```sh
source venv/bin/activate 
```
### Windows

Install the requeriments if doesn't exists.
```sh
pip install -r requirements.txt
```

Open the app.
```sh
python app.py
```
# recordar cambiar ip