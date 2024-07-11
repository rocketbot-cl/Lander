import os
import sys

"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

GetParams = GetParams
SetVar = SetVar
PrintException = PrintException

MODULE_NAME = "Lander"

base_path = tmp_global_obj["basepath"]
module_path = os.path.join(base_path, "modules", MODULE_NAME)
module_libs_path = os.path.join(module_path, "libs")

if module_libs_path not in sys.path:
    sys.path.append(module_libs_path)

SESSION_DEFAULT = "default"

global mod_lander_session

try:
    if not mod_lander_session:
        mod_lander_session = None
except NameError:
    mod_lander_session = None


from Lander import Lander

try:
    module = GetParams("module")  # Get command executed
    session = GetParams("session")  # Get Session name
    result = GetParams("result")  # Get variable name where save results

    if module == "connect":
        api_key = GetParams("api_key")
        host = GetParams("host")
        port = GetParams("port")
        rocketbot_path = GetParams("rocketbot_path")
        command_line = GetParams("command_line")

        if api_key and host and port and rocketbot_path:
            mod_lander_session = Lander(
                api_key, host, port, rocketbot_path, command_line
            )

            isConnected = mod_lander_session.connect()

            SetVar(result, True)  # this should return is Connected
        else:
            SetVar(result, False)
            raise ValueError(
                "API key, host, port and rocketbot_path are required fields"
            )

    elif module == "add_robot_to_queue":
        robot_name = GetParams("robot_name")
        execution_mode = GetParams("execution_mode")
        robot_command_params = GetParams("robot_command_params")
        robot_data = GetParams("robot_data")
        robot_db_path = GetParams("robot_db_path")

        if robot_name:
            res = mod_lander_session.add_robot_to_queue(
                robot_name,
                execution_mode,
                robot_command_params,
                robot_data,
                robot_db_path,
            )

            SetVar(result, res)

        else:
            SetVar(result, False)
            raise ValueError("robot_name is a required field")

    elif module == "run_robot":
        robot_id = GetParams("robot_id")
        execution_mode = GetParams("execution_mode")

        res = mod_lander_session.run_robot(robot_id, execution_mode)

        SetVar(result, res)

except Exception as e:
    result = GetParams("result")
    import traceback

    traceback.print_exc()
    SetVar(result, False)
    PrintException()
    raise e
