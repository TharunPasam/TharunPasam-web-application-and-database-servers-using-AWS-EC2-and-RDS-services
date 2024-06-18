import boto3

def configure_autoscaling():
    autoscaling = boto3.client('autoscaling')
    response = autoscaling.create_auto_scaling_group(
        AutoScalingGroupName='my-auto-scaling-grp',
        InstanceId='i-04fd0a8812f241692',  # Replace with your instance ID
        MinSize=1,
        MaxSize=3,
        DesiredCapacity=1,
        VPCZoneIdentifier='subnet-0ac8f61668865ede6,subnet-0b8c9216da6eaee8d',  # Replace with your subnets
        Tags=[
            {
                'ResourceId': 'my-auto-scaling-grp',
                'ResourceType': 'auto-scaling-group',
                'Key': 'Name',
                'Value': 'MyAutoScalingGroup',
                'PropagateAtLaunch': True
            }
        ]
    )
    print(f"Auto Scaling Group Created: {response}")

if __name__ == '__main__':
    configure_autoscaling()
