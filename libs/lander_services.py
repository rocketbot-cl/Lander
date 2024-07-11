import requests


class LanderServices:
    def __init__(
        self,
        api_key: str,
        host: str,
        port: str,
        rocketbot_path: str,
        command_line: str | None,
    ):
        self.api_key = api_key
        self.api_url = self.__build_url_api(host, port)

    def __build_url_api(self, host: str, port: str) -> str:
        return f"http://{host}:{port}"

    def connect(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}

        return requests.post(f"{self.api_url}/connect", headers=headers)

    def add_robot_to_queue(self, data: dict):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json; charset=utf-8",
        }

        return requests.post(f"{self.api_url}/add", headers=headers, json=data)
    
    def run_robot(self, data: dict):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json; charset=utf-8",
        }

        return requests.post(f"{self.api_url}/run", headers=headers, json=data)
