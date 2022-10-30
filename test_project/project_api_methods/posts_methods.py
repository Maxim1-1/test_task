from test_project.constants.endpoints import Endpoints
from test_project.project_utils.authorization_utils import AuthorizationUtils
from test_project.project_utils.parser_utils import UtilsParse
from base.api_utils import ApiUtils
from test_project.project_utils.urls_utils import UrlsUtils
import base64

CONFIG = UtilsParse().parse_config()


class PostMethods:
    auth = AuthorizationUtils().get_auth()

    def __init__(self, base_url, blog_id):
        self.base_url = base_url
        self.blog_id = blog_id

    def __get_url_for_request(self, endpoint, post_id=None):
        return UrlsUtils().create_url_for_request(obj_request='post', endpoint=endpoint, base_url=self.base_url,
                                                  blog_id=self.blog_id,
                                                  post_id=post_id)

    def get_post_info_by_id(self, post_id):
        url = self.__get_url_for_request(Endpoints.GET_INFO_POST_BY_ID, post_id)

        response = ApiUtils().get(url, auth=self.auth)

        return {"body": response.json(), "status_code": response.status_code,'msg':response.json()["meta"]["msg"]}

    def get_like_on_post(self):
        url = self.__get_url_for_request(Endpoints.VALIDATE_IK_ON_POST)
        response = ApiUtils().post(url, auth=self.auth)
        return response.json()

    def create_post(self, type_message, message, picture_path=None, title=None):
        url = self.__get_url_for_request(Endpoints.CREATE_POST)

        if type_message == 'text':
            data = {"type": "text",
                    "title": title,
                    "body": message
                    }
        elif type_message == 'photo':
            open_img = open(picture_path, 'rb')
            byte_img = base64.b64encode(open_img.read())
            data = {"type": "photo",
                    "caption": message,
                    "data64": byte_img}

        response = ApiUtils().post(url, auth=self.auth, data=data)
        status_code = response.status_code

        return {"body": response.json(), "status_code": status_code}

    def delete_post(self, post_id):
        url = self.__get_url_for_request(Endpoints.VALIDATE_IK_ON_POST)
        params = {"id": post_id}
        response = ApiUtils().post(url, auth=self.auth, data=params)
        status_code = response.status_code
        return {"body": response.json(), "status_code": status_code}

    def post_reblog(self, post_id, reblog_key, comment=None):
        url = self.__get_url_for_request(Endpoints.REBLOG_POST)
        params = {"id": post_id,
                  "reblog_key": reblog_key,
                  "comment": comment
                  }
        response = ApiUtils().post(url, auth=self.auth, data=params)

        return {"body": response.json(), "status_code": response.status_code}

    def edit_text_post(self, post_id, comment):
        url = self.__get_url_for_request(Endpoints.EDIT_TEXT)
        data = {"id": post_id,
                "body": comment
                }

        response = ApiUtils().post(url, auth=self.auth, data=data)
        return {"body": response.json(), "status_code": response.status_code}


