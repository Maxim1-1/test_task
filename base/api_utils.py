import requests


class ApiUtils:

    @staticmethod
    def get(url, stream=None, headers=None, auth=None, params=None):
        request = requests.get(url, headers=headers, auth=auth, params=params, stream=stream)
        return request

    @staticmethod
    def post(url, headers=None, data=None, json=None, auth=None):
        request = requests.post(url=url, headers=headers, json=json, data=data, auth=auth)
        return request

    @staticmethod
    def delete(url=None):
        request = requests.delete(url)

    @staticmethod
    def put(url=None):
        request = requests.put(url)
