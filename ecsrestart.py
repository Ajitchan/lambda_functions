import subprocess
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def run_command(command):
    command_list = command.split(' ')

    try:
        logger.info("Running shell command: \"{}\"".format(command))
        result = subprocess.run(command_list, stdout=subprocess.PIPE);
        logger.info("Command output:\n---\n{}\n---".format(result.stdout.decode('UTF-8')))
    except Exception as e:
        logger.error("Exception: {}".format(e))
        return False

    return True

def lambda_handler(event, context):
    run_command('/opt/aws ecs update-service --cluster jtp-cluster --service jtp-service --force-new-deployment')
    run_command('/opt/aws ecs update-service --cluster jtp-cluster --service fit-service --force-new-deployment')
    run_command('/opt/aws ecs update-service --cluster jtp-cluster --service service-prices-repository --force-new-deployment')
    run_command('/opt/aws ecs update-service --cluster jtp-cluster --service service-prices-collector --force-new-deployment')
    run_command('/opt/aws ecs update-service --cluster jtp-cluster --service service-result-calculation --force-new-deployment')