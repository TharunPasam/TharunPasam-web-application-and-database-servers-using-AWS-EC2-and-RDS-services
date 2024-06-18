import boto3

def setup_security_groups():
    ec2 = boto3.client('ec2')

    # Create Security Group
    response = ec2.create_security_group(
        GroupName='WebAppSecurityGroup',
        Description='Security group for web application',
        VpcId='vpc-0ffe05e7938ef73f0'  # Replace with your VPC ID
    )
    security_group_id = response['GroupId']
    print(f"Security Group Created: {security_group_id}")

    # Add Inbound Rules
    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 443,
                'ToPort': 443,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            }
        ]
    )
    print("Inbound Rules Set")

if __name__ == '__main__':
    setup_security_groups()
