# Automate Docker
A simple workflow to demonstrate docker automation using python script to run test in isolated environment and fetch the logs.

<br />

# Prerequisites
- Make sure you have docker installed and running by using the following command and receive a similar output:
```
Command: docker --version
Output: Docker version 24.0.7, build #######
```
- Make sure you have python installed and running by using the following command and receive a similar output:
```
Command: python --version
Output: Python 3.9.18
```

<br />

# Steps to Run
1. Clone this repository and change directory:
```
git clone https://github.com/ahmadhatahet/automate-docker-python.git

cd automate-docker-python
```

2. Install pip requirements
```
pip install -r requirement.txt
```

3. Run the following command:
```
python test_workflow_docker/main.py
```

<br />

# Expected Output (Log File)
```
2024-06-05T08:57:51.217447782Z test_boolean (test.test_sample.Testing) ... ok
2024-06-05T08:57:51.217473784Z test_string (test.test_sample.Testing) ... ok
2024-06-05T08:57:51.217475923Z
2024-06-05T08:57:51.217477214Z ----------------------------------------------------------------------
2024-06-05T08:57:51.217478516Z Ran 2 tests in 0.000s
2024-06-05T08:57:51.217479703Z
2024-06-05T08:57:51.217480823Z OK
```

<br />

# Modify for your specific case
In the file "main.py":
- Specify the image you would like to use instead of the current one "python:3.10.14-slim-bullseye".
- Change the directory to mount to docker instead of the current one "sample_code".
- Write the shell commands you want to run in the container in the variable "commands".
- Important to not remove the first line of the command "cd /code &&".
- Change the log file name or location based on your preferences.