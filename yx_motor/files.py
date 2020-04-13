# AUTOGENERATED! DO NOT EDIT! File to edit: 05_files.ipynb (unless otherwise specified).

__all__ = ['Files']

# Cell
import requests

from .api import API

class Files:
    "Class for handling authenticate API actions"

    def __init__(self, api: API):
        self.api = api
        self.base_endpoint = 'files/'

    def download_file(self, file_uuid: str, download_path: str):
        #TODO: MVP
        pass

    def upload_file(self):
        #TODO: MVP
        pass

    def update_file(self):
        #TODO: MVP
        pass

    def get_file_versions(self):
        pass

    def delete_file(self, hard=False):
        pass

    def copy_file(self, source_path: str, target_path: str):
        pass

    def move_file(self, source_path: str, target_path: str):
        #TODO: MVP
        pass

    def restore_deleted_file(self, asset_path: str=None, asset_id: str=None):
        pass