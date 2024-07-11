import requests
from constants import (LEETCODE_GRAPH_API,LEETCODE_API_PAYLOAD_v2, LEETCODE_PROFILE_API)


class MakeRequest:
    def __init__(self, username, payload):

        self.url = LEETCODE_GRAPH_API
        self.payload = payload
        self.username = username
        self.payload['variables']['username'] = self.username
        self.headers = {
            'Content-Type': 'application/json',
        }

    def get_data(self):
        try:
            response = requests.post(self.url, headers=self.headers, json=self.payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise Exception(err)
        