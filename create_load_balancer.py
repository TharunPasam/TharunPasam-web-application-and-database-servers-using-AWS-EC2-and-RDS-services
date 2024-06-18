import boto3

def create_load_balancer():
    elb = boto3.client('elbv2')
    response = elb.create_load_balancer(
        Name='my_lb',
        Subnets=['subnet-0ac8f61668865ede6', 'subnet-0b8c9216da6eaee8d'],  # Replace with your subnets
        SecurityGroups=['sg-0c7a1a359aec236ef'],  # Replace with your security group ID
        Scheme='internet-facing',
        Tags=[{'Key': 'Name', 'Value': 'MyLoadBalancer'}],
        Type='application',
        IpAddressType='ipv4'
    )
    lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
    print(f"Load Balancer Created: {lb_arn}")
    return lb_arn

if __name__ == '__main__':
    create_load_balancer()
