# AUTOGENERATED! DO NOT EDIT! File to edit: 01_motor.ipynb (unless otherwise specified).

__all__ = ['Motor']

# Cell
import requests

class Motor:
    "Wrapper for Alteryx Server API."

    def __init__(self,
                 base_url: str,
                 login_email: str,
                 login_pwd: str):

        self.base_url = base_url
        self.auth_url = f"{self.base_url}api/v1/authenticate"
        self.login_email = login_email
        self.login_pwd = login_pwd

        self.headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip,deflate"
        }

        self.jar = requests.cookies.RequestsCookieJar()
        self.is_authenticated = False
        self.authenticate()


    def authenticate(self) -> requests.Response:
        payload = {
            "email": self.login_email,
            "password": self.login_pwd
        }
        response = requests.post(url=self.auth_url,
                                 json=payload,
                                 cookies=self.jar,
                                 verify=False,
                                 headers=self.headers)
        if response.status_code == 200:
            self.jar.update(response.cookies)
            self.is_authenticated = True
            return response

    def get_jobs(self):
        response = requests.get(f"{self.base_url}api/v1/jobs",
                     cookies=self.jar,
                     verify=False)
        return response