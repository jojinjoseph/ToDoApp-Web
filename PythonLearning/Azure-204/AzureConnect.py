from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

"""This program will connect to your Azure subscription and try to print the group name.
Azure Subscription id to be set in the environmental variable """

subscription_id = "760c6e98-bb0a-4b43-865b-1b185ad20eb9" #Subscription id --az account show
credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, subscription_id)
print("client",client)
for rg in client.resource_groups.list():
    print(rg.name)