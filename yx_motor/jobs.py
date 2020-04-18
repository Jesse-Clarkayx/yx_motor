# AUTOGENERATED! DO NOT EDIT! File to edit: 02_jobs.ipynb (unless otherwise specified).

__all__ = ['Jobs']

# Cell
from .api import API


class Jobs:
    "class for all supported jobs APIs"


    def __init__(self, api: API):
        self.api = api
        self.base_endpoint = "jobs/"

    def get_job(self, jobid=""):
        response = self.api.get(url=f"{self.base_endpoint}{jobid}")
        return response

    def get_log(self, jobid):
        endpoint = "/logs"
        response = self.api.get(url=f"{self.base_endpoint}{jobid}{endpoint}")
        return response

    def cancel_job(self, jobid):
        endpoint = "/cancel"
        response = self.api.post(url=f"{self.base_endpoint}{jobid}{endpoint}")