from google.cloud import secretmanager_v1
import os
import json

class SecretManager:
    def __init__(self):
        self.client = secretmanager_v1.SecretManagerServiceClient()

    def access_secret_value(self, project_id, secret_name, version_id='latest'):
        name = f"projects/{project_id}/secrets/{secret_name}/versions/{version_id}"
        response = self.client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")

    def access_secret_json_file(self, project_id, secret_name, version_id='latest'):
        response = self.access_secret_value(project_id, secret_name, version_id='latest')
        dict_format = json.loads(response)
        return dict_format