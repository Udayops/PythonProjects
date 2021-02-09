import boto3
client = boto3.client('ec2')

resp = client.terminate_instances(InstanceIds=['i-001544b16bd7e41e3'])

for instance in resp['TerminatingInstances']:
    print("The instance with id {} Terminated".format(instance['InstanceId']))

