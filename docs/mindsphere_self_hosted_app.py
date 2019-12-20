""" Sample app for writing time series data to MindSphere. """
# Standard Library
from datetime import datetime
import json
import time
import random
# Additional Modules
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Enter your own asset ID here.
asset_id = "{myAssetID}"
# Enter your own Service Credentials here.
client_id = "{myServiceCredentialsClientID}"
client_secret = "{myServiceCredentialsClientSecret}"
# Enter your own MindSphere tenant name here.
tenant = "{myTenantName}"

# URL for the MindSphere IoT Time Series Service.
base_url = "https://gateway.eu1.mindsphere.io/api/iottimeseries/v3"
aspect = "MPL3115A2"
url = base_url + "/timeseries/" + asset_id + "/" + aspect

# Create a backend client and retrieve a token.
token_url = f"https://{tenant}.piam.eu1.mindsphere.io/oauth/token"
oauthclient = BackendApplicationClient(client_id=client_id)
oauthsession = OAuth2Session(client=oauthclient)
token = oauthsession.fetch_token(
    token_url=token_url,
    client_id=client_id,
    client_secret=client_secret
)

# Create an OAuth2Session object with the token.
client = OAuth2Session(client_id=client_id, token=token)

# Valid timestamp format is YYYY-mm-ddTHH:MM:SS.sssZ.
fmt = "%Y-%m-%dT%H:%M:%S.%f"

while True:
    # Form a valid timestamp.
    now = datetime.utcnow() # use UTC time
    timestamp = now.strftime(fmt)[:-3] + "Z"
    # All aspect’s variables should be written at the same time.
    timeseries = [
        {
            "_time": timestamp,
            "pressure": round(random.uniform(99000, 101325), 1),
            "temperature": round(random.uniform(20, 30), 3)
        }
    ]
    
    # Write the timeseries data.
    data = json.dumps(timeseries)
    headers = {"Content-Type": "application/json"}
    response = client.put(url, data=data, headers=headers)
    
    if response.status_code == 204:
        print("Timeseries written")
        print(json.dumps(timeseries, indent=4))
    
    time.sleep(30)
