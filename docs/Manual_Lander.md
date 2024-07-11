# Lander
  
This module is used to connect to Lander and execute commands.  

*Read this in other languages: [English](Manual_Lander.md), [Português](Manual_Lander.pr.md), [Español](Manual_Lander.es.md)*
  
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect to Lander
  

|Parameters|Description|example|
| --- | --- | --- |
|Add your Lander API key|Lander API key|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9|
|IP or host on which Lander is running|IP or host on which Lander is running|localhost|
|Port on which Lander is running|Port on which Lander is running|9999|
|Rocketbot executable path|Path to rocketbot.exe in the environment where Lander executes.|C:/Users/Usuario/Documents/Rocketbot_win_20240528/rocketbot.exe|
|Command line parameters|Extra parameters that will be passed to Rocketbot when running the Lander robots.|--log='log/path' --debug='false'|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Add robot to Lander queue
  
Add a robot to Lander queue
|Parameters|Description|example|
| --- | --- | --- |
|Robot name|Robot name|MyRobot|
|Execution mode|||
|Command line parameters|Extra parameters that will be passed to the command line in the execution of the robot.|--debug='false'|
|Extra information from the robot|Extra information that you want to send to the execution of the robot|{'times': 5, 'name': 'Jogn'}|
|Database path|Path to robot.db.|C:/Users/Usuario/Documents/Rocketbot_win_20240528/robot.db|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Run robot
  
Allows you to run a robot from the Lander queue
|Parameters|Description|example|
| --- | --- | --- |
|Robot ID|Robot ID|5|
|Execution mode|||
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|
