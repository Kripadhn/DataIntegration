import requests
import json
# Define the Log Analytics workspace ID and shared key
workspace_id = "<workspace-id>"
shared_key = "<shared-key>"

# Define the log data to be sent
log_data = [{
    "TimeGenerated": "2022-01-01T00:00:00.0000000Z",
    "Level": "Information",
    "Message": "This is a test log message."
}]

# Define the API endpoint and headers
endpoint = f"https://{workspace_id}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01"
headers = {
    "Content-Type": "application/json",
    "Log-Type": "TestLog"
}

# Compute the authorization signature
date = requests.utils.cookie_date(time.time())
string_to_hash = f"POST\n{len(json.dumps(log_data))}\napplication/json\nx-ms-date:{date}\n/api/logs"
bytes_to_hash = bytes(string_to_hash, "utf-8")  
key = base64.b64decode(shared_key)
signed_hmac_sha256 = hmac.HMAC(key, bytes_to_hash, hashlib.sha256)
authorization = f"SharedKey {workspace_id}:{base64.b64encode(signed_hmac_sha256.digest()).decode()}"
headers["Authorization"] = authorization
headers["x-ms-date"] = date

# Send the log data to Log Analytics
response = requests.post(endpoint, headers=headers, data=json.dumps(log_data))

# Check the response status code
if response.status_code != 200:
    raise Exception("Failed to send log data to Log Analytics.")
