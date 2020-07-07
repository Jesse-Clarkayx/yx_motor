# AUTOGENERATED! DO NOT EDIT! File to edit: 02_jobs.ipynb (unless otherwise specified).

__all__ = ['Jobs']

# Cell
from .api import API


class Jobs:
    "Class for tracking and managing jobs"

    def __init__(self, api: API):
        self.api = api
        self.base_endpoint = "jobs/"
        self.cancel_endpoint = "/cancel"
        self.log_endpoint = "/logs"

    def get_job(self, job_id: str = "", params=None):
        response = self.api.get(url=f"{self.base_endpoint}{job_id}", params=params)
        return response

    def get_log(self, job_id: str):
        response = self.api.get(url=f"{self.base_endpoint}{job_id}{self.log_endpoint}")
        return response

    def cancel_job(self, job_id: str):
        response = self.api.post(
            url=f"{self.base_endpoint}{job_id}{self.cancel_endpoint}"
        )
        return response