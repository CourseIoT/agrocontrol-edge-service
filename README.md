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
--------------

### Linux:
Enter to the virtual environment. 
```sh
source venv/bin/activate 
```
### Windows
To enable the script executión in the sessión
Use in the PowerShell
```sh
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:
```sh
venv\Scripts\Activate.ps1
```
--------------

Install the requeriments if doesn't exists.
```sh
pip install -r requirements.txt
```

Open the app.
```sh
python app.py
```
# recordar cambiar ip
