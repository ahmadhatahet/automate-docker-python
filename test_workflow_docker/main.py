from pathlib import Path
from docker_utils import create_and_run_container, save_docker_log

...

if __name__ == "__main__":
    # directory to mount
    path = Path(__file__).parent / "sample_code"

    # image to pull and run test with in
    image = "python:3.10.14-slim-bullseye"

    # shell command to execute in the container
    commands = '''
        cd /code &&
        python -m unittest -v
    '''

    # file to save docker log
    log_folder = Path(__file__).parent / "docker_log"
    log_folder.mkdir(exist_ok=True)

    log_file = log_folder / "docker_log.txt"

    # run container
    container, container_result, log = create_and_run_container(image, path, commands)

    # save log if not None
    if log is not None: save_docker_log(log_file, log)