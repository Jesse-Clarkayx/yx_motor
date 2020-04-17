# AUTOGENERATED! DO NOT EDIT! File to edit: 05_files.ipynb (unless otherwise specified).

__all__ = ['Files']

# Cell
import requests

from .api import API


class Files:
    "Class for handling Files endpoints"

    def __init__(self, api: API):
        self.api = api
        self.base_endpoint = "files/"

    def download_file(self, file_uuid: str, download_path: str, version: int = None):
        response = self.api.get(
            url=f'{self.base_endpoint}content', params={"id": file_uuid,"version": version}
        )
        with open(download_path, 'wb') as f:
            f.write(response.content)
        return response

    def upload_file(
        self,
        filename: str,
        upload_path: str,
        description: str = "",
        conflict_action=None,
    ):
        upload_headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip,deflate",
            "path": f"{upload_path}",
            "description": f"{description}",
            "conflict_action": f"{conflict_action}",
        }

        with open(filename, "rb") as f:
            blob = f.read()
        response = self.api.post(url=f"{self.base_endpoint}", data=blob, non_default_headers=upload_headers)
        return response

    def update_file(self):
        # This seems to update metainfo, may not be needed for MVP
        # TODO: MVP
        pass

    def get_file_versions(self, file_uuid: str):
        response = self.api.get(url=f"{self.base_endpoint}versions/", params={"id": file_uuid})
        return response

    def delete_file(self, asset_path: str, hard=False):
        payload = {"assetPaths": [f"{asset_path}"]}

        if hard == True:
            targeturl = "remove"
        else:
            targeturl = "softDelete"

        response = self.api.post(url=f'{self.base_endpoint}{targeturl}', data=payload)

        return response

    def move_file(
        self,
        source_path: str,
        target_path: str,
        move_type="move",
        versions_action="ALL_VERSIONS",
        conflicts_action="SKIP",
    ):
        # TODO discuss move_type, move or copy
        payload = {
            "assets": [
                {"sourcePath": f"{source_path}", "targetPath": f"{target_path}"}
            ],
            "targetPath": "string",
            "versionsAction": f"{versions_action}",
            "conflictsAction": f"{conflicts_action}",
        }

        response = self.api.post(url=f'{self.base_endpoint}{move_type}', data=payload)
        return response

    def restore_deleted_file(self, asset_path: str = None, asset_id: str = None):
        asset_paths = {}
        asset_ids = {}
        if asset_path:
            asset_paths = {"assetPaths": [f"{asset_path}"]}
        if asset_id:
            asset_ids = {"assetIds": [f"{asset_id}"]}
        payload = {**asset_paths, **asset_ids, **{"onlyDescendants": True}}
        response = self.api.post(url=f"{self.base_endpoint}restoreDeleted", data=payload)
        return response