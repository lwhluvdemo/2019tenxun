import azureml.core
from azureml.core import Workspace, Datastore

ws = Workspace.from_config()

ds = ws.get_default_datastore()
print(ds)

#list all datastores registered in current workspace
datastores = ws.datastores
for name, ds in datastores.items():
    print(name, ds.datastore_type)

import azureml.data
from azureml.data.azure_storage_datastore import AzureFileDatastore, AzureBlobDatastore

ds.upload(src_dir="D:\\tenxun\\algo.qq.com_641013010_testa\\testA",
          target_path="testa",
          overwrite=True,
          show_progress=True)