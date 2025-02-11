# import boto3
# def create_ec2_instance():
#     try:
#         print("Creating EC2 instance")
#         resource_ec2 = boto3.client("ec2")
#         resource_ec2.run_instances(
#             ImageId="ami-0ad704c126371a549",
#             MinCount=1,
#             MaxCount=1,
#             InstanceType="t2.micro",
#             KeyName="ec2-keypair"
#         )
#     except Exception as e:
#             print(e)
        
# create_ec2_instance()

