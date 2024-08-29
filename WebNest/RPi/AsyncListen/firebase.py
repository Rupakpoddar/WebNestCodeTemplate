'''
Written by Rupak Poddar
https://rupakpoddar.github.io/
'''

import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("myFirebaseKey.json")
firebase_admin.initialize_app(
    cred, {"databaseURL": "YOUR FIREBASE REALTIME DATABASE REFERENCE URL GOES HERE"}
)

# Reference to a specific node in the database
data_ref = db.reference("")

# Function to be called when the data is written
def on_value_written(event):
    print("%s: %s" %(event.path, event.data))

# Set up the listener for the on_value_written event
data_ref.listen(on_value_written)

# Example: Update data to the database
def update_data(data):
    data_ref.update(data)
    print("Data updated successfully!")

update_data({'MyLight':{'State': 1}})

# Example: Write data to the database (replaces existing data)
def write_data(data):
    data_ref.set(data)
    print("Data written successfully!")

# write_data({'DeskLamp':{'State': 1}})

# Keep the program running to listen for events
while True:
    pass

