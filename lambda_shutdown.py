import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    filters = [{
            'Name': 'tag:development',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    instances = ec2.instances.filter(Filters=filters)
    RunningInstances = [instance.id for instance in instances]
    for instance_id in RunningInstances:
        ec2.instances.stop(InstanceIds=[instance_id])
