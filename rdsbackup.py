# Create Delete 23 00

import subprocess
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

snapshot = "engie-uk-prod"
snapshot_copy = "engie-uk-prod-jtp"
account = "957459130976"
sour_account = "358715644539"
sour_region = "eu-west-2"
dest_region = "eu-west-2"
kms = "arn:aws:kms:eu-west-2:358715644539:key/mrk-af019307b29f40708adbe32766f6e45a"

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
    run_command('/opt/aws rds delete-db-snapshot --db-snapshot-identifier ' + snapshot + '')
    run_command('/opt/aws rds delete-db-snapshot --db-snapshot-identifier ' + snapshot_copy + ' --region ' + dest_region + '')
    run_command('/opt/aws rds create-db-snapshot --db-instance-identifier jtp --db-snapshot-identifier ' + snapshot + '')
    #run_command('/opt/aws rds copy-db-snapshot --source-db-snapshot-identifier ' + 'arn:aws:rds:' + sour_region + ':' + sour_account + ':snapshot:' + snapshot + ' --kms-key-id ' + kms + ' --target-db-snapshot-identifier ' + snapshot_copy + ' --region ' + dest_region + '')
    #run_command('/opt/aws rds modify-db-snapshot-attribute --db-snapshot-identifier ' + snapshot_copy + ' --attribute-name restore --values-to-add ' + account + ' --region ' + dest_region + '')
    #run_command('/opt/aws rds delete-db-snapshot --db-snapshot-identifier ' + snapshot + '')
	

# Copy 23 15

import subprocess
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

snapshot = "engie-uk-prod"
snapshot_copy = "engie-uk-prod-jtp"
account = "957459130976"
sour_account = "358715644539"
sour_region = "eu-west-2"
dest_region = "eu-west-2"
kms = "arn:aws:kms:eu-west-2:358715644539:key/mrk-af019307b29f40708adbe32766f6e45a"

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
    #run_command('/opt/aws rds delete-db-snapshot --db-snapshot-identifier ' + snapshot + '')
    #run_command('/opt/aws rds delete-db-snapshot --db-snapshot-identifier ' + snapshot_copy + ' --region ' + dest_region + '')
    #run_command('/opt/aws rds create-db-snapshot --db-instance-identifier jtp --db-snapshot-identifier ' + snapshot + '')
    run_command('/opt/aws rds copy-db-snapshot --source-db-snapshot-identifier ' + 'arn:aws:rds:' + sour_region + ':' + sour_account + ':snapshot:' + snapshot + ' --kms-key-id ' + kms + ' --target-db-snapshot-identifier ' + snapshot_copy + ' --region ' + dest_region + '')
    #run_command('/opt/aws rds modify-db-snapshot-attribute --db-snapshot-identifier ' + snapshot_copy + ' --attribute-name restore --values-to-add ' + account + ' --region ' + dest_region + '')
    #run_command('/opt/aws rds delete-db-snapshot --db-snapshot-identifier ' + snapshot + '')

# Update account 0 10


import subprocess
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

snapshot = "engie-uk-prod"
snapshot_copy = "engie-uk-prod-jtp"
account = "957459130976"
sour_account = "358715644539"
sour_region = "eu-west-2"
dest_region = "eu-west-2"
kms = "arn:aws:kms:eu-west-2:358715644539:key/mrk-af019307b29f40708adbe32766f6e45a"

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
    #run_command('/opt/aws rds delete-db-snapshot --db-snapshot-identifier ' + snapshot + '')
    #run_command('/opt/aws rds delete-db-snapshot --db-snapshot-identifier ' + snapshot_copy + ' --region ' + dest_region + '')
    #run_command('/opt/aws rds create-db-snapshot --db-instance-identifier jtp --db-snapshot-identifier ' + snapshot + '')
    #run_command('/opt/aws rds copy-db-snapshot --source-db-snapshot-identifier ' + 'arn:aws:rds:' + sour_region + ':' + sour_account + ':snapshot:' + snapshot + ' --kms-key-id ' + kms + ' --target-db-snapshot-identifier ' + snapshot_copy + ' --region ' + dest_region + '')
    run_command('/opt/aws rds modify-db-snapshot-attribute --db-snapshot-identifier ' + snapshot_copy + ' --attribute-name restore --values-to-add ' + account + ' --region ' + dest_region + '')
    run_command('/opt/aws rds modify-db-snapshot-attribute --db-snapshot-identifier ' + snapshot_copy + ' --attribute-name restore --values-to-add 251790535227 +  --region ' + dest_region + '')
    run_command('/opt/aws rds delete-db-snapshot --db-snapshot-identifier ' + snapshot + '')