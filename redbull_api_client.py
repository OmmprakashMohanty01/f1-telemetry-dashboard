import requests
import logging

logger = logging.getLogger(__name__)


import requests
import json


class RacingAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.example.com"

    def get_live_telemetry(self, session_id):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        params = {"session": session_id}
        response = requests.get(
            f"{self.base_url}/live-telemetry", headers=headers, params=params
        )
        return response.json()

    def get_lap_times(self, session_id):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        params = {"session": session_id}
        response = requests.get(
            f"{self.base_url}/lap-times", headers=headers, params=params
        )
        return response.json()

    def get_lap_data(self, session_id, driver_id):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        params = {"session": session_id, "driver": driver_id}
        response = requests.get(
            f"{self.base_url}/lap-data", headers=headers, params=params
        )
        return response.json()


class RacingAPIClient:
    def __init__(self, api_key):
        self.api = RacingAPI(api_key)

    def fetch_live_telemetry(self, session_id):
        return self.api.get_live_telemetry(session_id)

    def fetch_lap_times(self, session_id):
        return self.api.get_lap_times(session_id)

    def fetch_lap_data(self, session_id, driver_id):
        return self.api.get_lap_data(session_id, driver_id)


# Usage
client = RacingAPIClient("YOUR_API_KEY")
session_id = "SESSION_ID"
driver_id = "DRIVER_ID"
live_telemetry = client.fetch_live_telemetry(session_id)
lap_times = client.fetch_lap_times(session_id)
lap_data = client.fetch_lap_data(session_id, driver_id)


class TelemetryAPIClient:
    def fetch_driver_status(self, driver_id):
        return self.api.get_driver_status(driver_id)


class DriverAPIClient:
    def fetch_driver_history(self, driver_id):
        return self.api.get_driver_history(driver_id)


class EventAPIClient:
    def fetch_event_schedule(self, event_id):
        return self.api.get_event_schedule(event_id)

    def fetch_event_results(self, event_id):
        return self.api.get_event_results(event_id)
