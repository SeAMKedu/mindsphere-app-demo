""" Publish data to MindConnect IoT Extension. """
# Standard Library
import time
# Additional Modules
import paho.mqtt.client as mqtt

# Configurations.
CLIENT_ID = "myClientID"
USERNAME = "myTenant/myMCIoTExtensionUsername"
PASSWORD = "myPassword"
HOST = "mciotextension.eu-central.mindsphere.io"
PORT = 1883
TOPIC = "s/us"

def on_connect(client, userdata, flags, rc):
    """ Callback for when the client receives a CONNACK response from the server. """
    print("Connected with the result code: " + str(rc))

def main():
    # Create a MQTT Client instance.
    client = mqtt.Client(client_id=CLIENT_ID)

    # Set callback functions.
    client.on_connect = on_connect

    # Set username and password.
    client.username_pw_set(USERNAME, password=PASSWORD)

    # Connect to the server.
    try:
        client.connect(HOST, port=PORT)
    except ConnectionRefusedError as error:
        print(error)

    # Create a new device: "100,<deviceName>,<deviceType>"
    #client.publish(TOPIC, payload="100,PysenseMQTT,MCIoT_MQTTDevice")

    # Manage device information: "110,<serialNumber>,<hardwareModel>,<revision>"
    #client.publish(TOPIC, payload="110,1737000142,Pysense,1.1")

    # Set device location: "112,<lat>,<long>,<altitude>,<accuracy>"
    #client.publish(TOPIC, payload="112,62.788810,22.822477")

    # Create custom measurement: "200,<fragment>,<series>,<value>,<unit>,<timestamp>"
    client.publish(TOPIC, payload="200,pressure,Pascal,99340.4,Pa")

    time.sleep(1)
    # Disconnect from the server.
    client.disconnect()

if __name__ == '__main__':
    main()
