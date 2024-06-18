import boto3

def create_ec2_instance():
    ec2 = boto3.resource('ec2',  region_name='us-east-1')
    instances = ec2.create_instances(
        ImageId='ami-08a0d1e16fc3f61ea',  # Replace with a valid AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='inst1',  # Replace with your key pair name
        SecurityGroupIds=['sg-0c7a1a359aec236ef'],  # Replace with your security group ID
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'WebServer'}]
            }
        ]
    )
    instance_id = instances[0].id
    print(f"EC2 Instance Created: {instance_id}")
    return instance_id

if __name__ == '__main__':
    create_ec2_instance()