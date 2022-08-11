#Creating EC2 instance using Python 3 with Boto3

'''
enter your aws access key id,
aws secret access key,
region name(ap-south-1)
output format(json)
'''

#importing boto3
import boto3

def creating_ec2_instance():
    try:
        print("Creating EC2 instances.....")
        var_1 = boto3.client("ec2")
        var_1.run_instances(
            ImageId = "**************", # Ami id
    # keep this min and max count as your wish,
    # here i'm taking 1.
            MinCount = 1,
            MaxCount = 1,
            InstanceType = "*****",
            KeyName = "*****"
        )
        print("EC2 instance created")


    except Exception as e:
        print(e)

creating_ec2_instance()




