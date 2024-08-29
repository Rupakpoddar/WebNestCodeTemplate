"""
Instructions to use WebNest with Firebase Realtime Database:

1. Ensure you have the Firebase Admin SDK properly set up by downloading your service account key file.
2. Replace the path to your service account key file in the `Certificate` method.
3. Replace the placeholder in the `databaseURL` with your Firebase Realtime Database URL, e.g., `https://your-database.firebaseio.com/`.
4. The script will interact with the Firebase Realtime Database to update and read device states.
5. Go to the following link in your web browser: https://rupakpoddar.github.io/WebNest/
6. In the WebNest interface, click the gear icon on the top right to open the setup tab.
7. Paste the Firebase database URL (e.g., `https://your-database.firebaseio.com/`) into the "Service URL/IP" field and click "Update."
8. Click the add button (top right) to create a new device. For this example:
    - Create a device with the name "BedroomLight" (without quotes).
    - Choose the button style (ON/OFF or Toggle).
    - Select the desired parameters like color, temperature, and pwm.
    - Click "Finish" to create the new WebNest device.
9. Repeat the same process to create additional devices like "TableFan" and "DeskLamp."

Once configured, the WebNest interface will interact with your Firebase database to control devices remotely.

"""

import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK with the service account key
cred = credentials.Certificate("my_firebase_key.json")
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://your-database.firebaseio.com/"}
)

# Reference the root of the database
data_ref = db.reference("")

def on_value_written(event):
    """
    Callback function triggered when data is written to Firebase.

    Args:
        event (object): Contains information about the data that was written (path, data).
    """
    print(f"{event.path}: {event.data}")

# Set up a listener to monitor changes in the database and trigger the callback
data_ref.listen(on_value_written)

def update_data(data):
    """
    Update existing data in the Firebase Realtime Database.
    
    Args:
        data (dict): The data to be updated (key-value pairs).
    """
    data_ref.update(data)
    print("Data updated successfully!")

# Example: Updating the state of a device in the database
# update_data({'TableFan': {'State': 1}})

def write_data(data):
    """
    Write new data to the Firebase Realtime Database (replaces existing data at the node).
    
    Args:
        data (dict): The data to be written (key-value pairs).
    """
    data_ref.set(data)
    print("Data written successfully!")

# Example: Writing the state of a device in the database
# write_data({'DeskLamp': {'State': 1}})

# Keep the program running indefinitely to listen for database events
while True:
    pass
