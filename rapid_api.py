import http.client
import json

class __API_Connection:
    URL: str

    def __init__(self, endpoint: str, protocol: str = "GET") -> None:
        self.endpoint = endpoint
        self.protocol = protocol
        self.headers = {
            'X-RapidAPI-Key': json.load(open('config.json','r'))['X-RapidAPI-Key'],
            'X-RapidAPI-Host': self.URL,
            'Content-Type': "application/json"
        }

    def send_json(self, payload: str = "") -> str:
        conn = http.client.HTTPSConnection(self.URL)
        headers = self.headers
        # payload = payload.replace('\n', '')
        conn.request(self.protocol, self.endpoint, payload, headers)
        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")


class API_Football(__API_Connection):
    URL: str = "api-football-v1.p.rapidapi.com"

class Arbitrage_Betting_Calculator(__API_Connection):
    URL: str = "arbitrage-betting-calculator.p.rapidapi.com"
