from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import os

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, subscription_id)
print("client",client)
for rg in client.resource_groups.list():
    print(rg.name)