import boto3

# client = boto3.client('ec2')
# response = client.describe_instances()
# # print(response)

# for instance in response["Reservations"][0]['Instances']:
#     print(instance["InstanceId"])

ec2 = boto3.resource('ec2')


def create_instance(name=""):
    ec2.create_instances(
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': name
                    },
                ]
            },
        ],
        InstanceType='t2.micro',
        ImageId='ami-0c4e4b4eb2e11d1d4',
        MaxCount=1,
        MinCount=1
    )


def delete_instance(instance_id):
    ec2.instances.filter(InstanceIds=[instance_id]).terminate()


def get_instances_ids():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for instance in response["Reservations"]:
        for id in instance['Instances']:
            print(id["InstanceId"])


# create_instance(input("Hey.. please enter th name of the instance:\n"))
# delete_instance(input("What instance do you want to delete?\n"))
get_instances_ids()
