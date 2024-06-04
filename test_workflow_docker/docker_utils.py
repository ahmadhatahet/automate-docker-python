from pathlib import Path
import docker
from docker.errors import APIError, ContainerError


def get_client():
    """Connect to docker daemon"""
    return docker.from_env()

def list_images():
    """List all available images"""
    client = get_client()
    return client.images.list()

def list_containers():
    """List all available containers"""
    client = get_client()
    return client.containers.list()

def create_and_run_container(image: str, directory: Path, commands: str):
    """Run a specific container and mount a directory to "/code"
    then execute the command passed as an argument then return the logs and remove container"""
    # Connects to Docker daemon
    client = get_client()

    try:
        # Pull the image
        client.images.pull(image)

        # Run the container & execute commands
        container = client.containers.run(
            image,
            command=f"/bin/sh -c '{commands}'",
            volumes={str(directory): {'bind': '/code', 'mode': 'rw'}},
            working_dir="/code",
            # remove=True, # Does not work within the run function, must be separate
            detach=True,
            tty=True
        )
        print(f"Container {container.id} created and running")

        # Wait for the container to finish running
        container_result = container.wait()

        # Capture output (both stdout and stderr)
        output = container.logs(stream=False, stdout=True, stderr=True, timestamps=True).decode()
        print(output)

        # Clean up the container when the container exits
        container.remove()

        return container, container_result, output

    except APIError as e:
        print(f"API Error: {e.explanation}")
    except ContainerError as e:
        print(f"Container Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    return None, None, None

def save_docker_log(filepath: Path, log: str):
    filepath.touch()

    with filepath.open("w") as f:
        f.write(log)
