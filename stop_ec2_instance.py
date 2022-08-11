#Stop EC2 instance using Python 3 with Boto3

'''
enter your aws access key id,
aws secret access key,
region name(ap-south-1)
output format(json)
'''

#importing boto3
import boto3

def getting_instance_id():
    try:
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)

def stop_ec2_instance():
    try:
        print ("Stop EC2 instance")
        instance_id = getting_instance_id()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)
# calling the function.
stop_ec2_instance()




