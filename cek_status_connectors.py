import requests
import json

def check_connector_status(connector_name):
    connect_url = f"http://localhost:8083/connectors/{connector_name}/status"
    response = requests.get(connect_url)

    if response.status_code == 200:
        status = response.json()
        print(json.dumps(status, indent=4))
    else:
        print(f"Failed to get status for connector '{connector_name}': {response.status_code}, {response.text}")

if __name__ == "__main__":
    connector_name = "exampledb2-connector"
    check_connector_status(connector_name)
