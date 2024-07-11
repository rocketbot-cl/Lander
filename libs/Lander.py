import ast

from lander_services import LanderServices


class Lander:
    def __init__(
        self,
        api_key: str,
        host: str,
        port: str,
        rocketbot_path: str,
        command_line: str | None,
    ):
        self.services = LanderServices(
            api_key, host, port, rocketbot_path, command_line
        )

    def connect(self) -> bool:

        res = self.services.connect()
        return res.ok

    def add_robot_to_queue(
        self,
        robot_name: str,
        execution_mode: str,
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
            "mode": execution_mode,
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
