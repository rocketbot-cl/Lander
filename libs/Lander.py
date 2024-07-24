import ast
import configparser

from lander_services import LanderServices


class Lander:
    def __init__(
        self,
        lander_folder_path: str,
        api_key: str,
    ):
        self.lander_folder_path = lander_folder_path
        self.api_key = api_key
        self.services = None

    def connect(self) -> bool:
        api_key, host, port, rocketbot_path, command_line, db_path = (
            self.__get_lander_config()
        )

        self.services = LanderServices(
            api_key, host, port, rocketbot_path, command_line
        )

        return bool(self.services)

    def __get_lander_config(self) -> tuple:
        config = configparser.ConfigParser()
        config.read(f"{self.lander_folder_path}/config.ini")

        api_key, host, port, rocketbot_path, command_line, db_path = (
            self.api_key,
            config["server"]["host"],
            config["server"]["port"],
            config["rocketbot"]["path"],
            config["rocketbot"]["params"],
            config["db"]["path"],
        )

        return api_key, host, port, rocketbot_path, command_line, db_path

    def add_robot_to_queue(
        self,
        robot_name: str,
        command_params: str,
        extra_data: str,
        robot_db_path: str,
        run=False,
    ) -> dict:

        dict_extra_data = ast.literal_eval(extra_data) if extra_data is not None else ""
        parsed_command_params = command_params

        if robot_db_path:
            parsed_command_params = command_params + " " + f"-db='{robot_db_path}'"

        req_body = {
            "robot": robot_name,
            "run": run,
            "command_params": parsed_command_params,
            "data": dict_extra_data,
        }
        res = self.services.add_robot_to_queue(req_body)

        if res.ok:
            return res.json()

        return {"error": res.text, "status": "failed"}

    def run_robot(self, robot_id: str, mode="wait") -> dict:
        req_body = {"id": robot_id, "mode": mode}
        res = self.services.run_robot(req_body)

        if res.ok:
            return res.json()

        return {"error": res.text, "status": "failed"}
