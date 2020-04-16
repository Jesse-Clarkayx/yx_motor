# AUTOGENERATED! DO NOT EDIT! File to edit: 03_api.ipynb (unless otherwise specified).

__all__ = ['API', 'default_headers']

# Cell
import requests

# from yx_motor import logger, config, version

default_headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip,deflate",
}


class API(object):
    def __init__(self, api_url, headers=None):
        self.api_url = api_url
        headers = headers or default_headers
        self.headers = headers.copy()
        self.is_authenticated = False
        self.jar = requests.cookies.RequestsCookieJar()

    def get_path(self, url):
        api_url = self.api_url if not self.api_url.endswith("/") else self.api_url[:-1]
        template = "{}{}" if url.startswith("/") else "{}/{}"
        return template.format(api_url, url)

    def post(
        self,
        url,
        json=None,
        params=None,
        files=None,
        data=None,
        cookies=None,
        verify=False,
        non_default_headers=None,
    ):
        if not cookies:
            cookies = self.jar
        path = self.get_path(url)
        #         logger.debug("POST request sent to: {} \n\theaders: {}\n\tjson: {}\n\tparams: {}\n\tfiles: {}\n\tdata: {}"
        #                      .format(path, self.headers, json, params, files, data))
        if non_default_headers:
            headers = non_default_headers
        else:
            headers = self.headers

        response = requests.post(
            path,
            json=json,
            params=params,
            headers=headers,
            files=files,
            data=data,
            cookies=cookies,
            verify=verify,
        )
        #         logger.debug("Response status code: {}".format(response.status_code))
        #         logger.debug("Response content: {}".format(response.content))
        return response

    def put(self, url, json=None, params=None):
        path = self.get_path(url)
        logger.debug(
            "PUT request sent to: {} \n\theaders: {}\n\tjson: {}\n\tparams: {}".format(
                path, self.headers, json, params
            )
        )
        response = requests.put(path, json=json, params=params, headers=self.headers)
        #         logger.debug("Response status code: {}".format(response.status_code))
        #         logger.debug("Response content: {}".format(response.content))
        return response

    def get(
        self,
        url,
        json=None,
        params=None,
        files=None,
        data=None,
        cookies=None,
        verify=False,
    ):
        if not cookies:
            cookies = self.jar
        path = self.get_path(url)
        #         logger.debug("GET request sent to: {} \n\theaders: {}\n\tjson: {}\n\tparams: {}"
        #                      .format(path, self.headers, json, params))
        response = requests.get(
            path,
            params=params,
            headers=self.headers,
            json=json,
            files=files,
            data=data,
            cookies=cookies,
            verify=verify,
        )
        #         logger.debug("Response status code: {}".format(response.status_code))
        #         logger.debug("Response content: {}".format(response.content))
        return response

    def delete(self, url, json=None, params=None):
        path = self.get_path(url)
        response = requests.delete(path, params=params, headers=self.headers, json=json)
        #         logger.debug("DELETE request sent to: {} \n\theaders: {}\n\tjson: {}\n\tparams: {}"
        #                      .format(response.url, self.headers, json, params))
        #         logger.debug("Response status code: {}".format(response.status_code))
        #         logger.debug("Response content: {}".format(response.content))
        return response