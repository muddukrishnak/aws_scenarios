# aws_scenarios

- Python version - Python 3.7.0

## Setup virtual environment

### Windows

- Run bellow connamds in command prompt.
- ```pip install virtualenv``` -> This installs virtual environment.
- ```cd {to_project_path}``` -> Go into your projrct folder.
- ```C:\Users\{user_name}\AppData\Local\Programs\Python\Python37\Scripts\virtualenv vrtul_env```  -> Create a virtual environment named vrtul_env.
- ```.\vrtul_env\Scripts\activate```  -> Actiavate the virtual environment.
- ```pip freeze > requirements.txt```  -> Create a requirments files with all the installed packages.
- ```pip install -r requirements.txt```  -> Install all the packages that are specified in requirments file.
- ```deactivate``` -> Deactivate from virtual environment.

### Mac/Linux

## AWS login setup

### Wnidows

- Launch "Control Panel" -> Search(ctrl+f) for "Environment variables" -> "Edit the system environment variables" -> Switch to "Advanced" tab -> "Environment variables"
- Choose one of User variables(only you can access) or System variables(all users can access)
- Choose "New"
- Enter the variable "Name" (aws_access_key) and "Value" (get access key from AWS IAM)
- Enter the variable "Name" (aws_secret_key) and "Value" (get secret key from AWS IAM)
- To change an existing environment variable:
- Choose "Edit"
- Enter the new "Value"
- You need to RE-START CMD for the new setting to take effect!

### Mac/Linux
