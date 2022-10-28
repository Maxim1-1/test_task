from base.api_utils import ApiUtils
from test_project.constants.endpoints import Endpoints
from test_project.dummy_utils.parser_utils import UtilsParse

CONFIG = UtilsParse.parse_config()


class DummyApiMethods:

    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self):
        headers = {"app-id": CONFIG["token"]}

        url = f"{self.base_url}{Endpoints.create_user}"
        data = {"firstName": "f2wegf",
                "lastName": "dfweg2df",
                "email": "dfgswes2dfg@yandex.com"}

        response = ApiUtils().post(url, headers=headers, data=data)
        return response

    def create_post(self, user, message):
        headers = {"app-id": CONFIG["token"]}

        url = f"{self.base_url}{Endpoints.create_post}"
        data = {"owner": user,
                "text": message
                }

        response = ApiUtils().post(url, headers=headers, data=data)
        return response

    def get_post_by_id(self, post_id):
        headers = {"app-id": CONFIG["token"]}

        url = f"{self.base_url}{Endpoints.get_info_post_by_id.format(post_id=post_id)}"

        response = ApiUtils().get(url, headers=headers)
        return response

    def create_comment(self, user, message_comment):
        headers = {"app-id": CONFIG["token"]}

        url = f"{self.base_url}{Endpoints.create_comment}"
        data = {"id": "635c01205965420258c3abce",
                "message": message_comment,
                # "post": "635c01205965420258c3abce"

                }

        response = ApiUtils().post(url, headers=headers, data=data)
        return response


# s = DummyApiMethods('https://dummyapi.io/data/v1').get_post_by_id('635c01205965420258c3abce')
g = DummyApiMethods('https://dummyapi.io/data/v1').create_post('635bfe7959654266a5c3ab45', 'new mes')
com = DummyApiMethods('https://dummyapi.io/data/v1').create_comment('635bfe7959654266a5c3ab45','lalallala')
print(com.json())

# 635c01205965420258c3abce