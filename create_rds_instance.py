import boto3

def create_rds_instance():
    rds = boto3.client('rds')
    response = rds.create_db_instance(
        DBName='mydb',
        DBInstanceIdentifier='mydbinst',
        AllocatedStorage=20,
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        MasterUsername='dbuser',
        MasterUserPassword='mydb2710',  # Replace with your password
        VpcSecurityGroupIds=['sg-0c7a1a359aec236ef'],  # Replace with your security group ID
        Tags=[
            {'Key': 'Name', 'Value': 'MyRDSInstance'}
        ]
    )
    print(f"RDS Instance Created: {response['DBInstance']['DBInstanceIdentifier']}")
    return response['DBInstance']['DBInstanceIdentifier']

if __name__ == '__main__':
    create_rds_instance()
