from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.consts import WORK_DIR,DOCKER_TIMEOUT


def getDockerCommandLineCodeExecutor():
    docker = DockerCommandLineCodeExecutor(
        work_dir=WORK_DIR,
        timeout=DOCKER_TIMEOUT,
        image="amancevice/pandas"
    )

    return docker

async def start_docker(docker):
    print("Starting Docker Container")
    await docker.start()
    print("Docker Container Started")

async def stop_docker(docker):
    print("Stoping Docker Container")
    await docker.stop()
    print("Docker Container Stopped")

