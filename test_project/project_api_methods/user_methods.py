from test_project.project_utils.parser_utils import UtilsParse
from base.api_utils import ApiUtils
from test_project.project_utils.authorization_utils import AuthorizationUtils
from test_project.constants.endpoints import Endpoints
from test_project.project_utils.urls_utils import UrlsUtils

CONFIG = UtilsParse().parse_config()


class UserMethods:

    auth = AuthorizationUtils().get_auth()

    def __init__(self, base_url, blog_id):
        self.base_url = base_url
        self.blog_id = blog_id

    def __get_url_for_request(self, endpoint, post_id=None):
        return UrlsUtils().create_url_for_request(obj_request='user', endpoint=endpoint, base_url=self.base_url,
                                                  blog_id=self.blog_id,
                                                  post_id=post_id)

    def set_like_on_post(self, post_id, reblog_key):
        url = self.__get_url_for_request(Endpoints.SET_LIKE_ON_POST)

        params = {"id": post_id,
                  "reblog_key": reblog_key}
        response = ApiUtils().post(url, auth=self.auth, data=params)

        return response.json()

    def get_user_blogs(self):

        url = self.__get_url_for_request(Endpoints.FOLLOWING_USERS)
        response = ApiUtils().post(url, auth=self.auth)
        return {"body": response.json(), "status_code": response.status_code}



# s = UserMethods('https://api.tumblr.com','test-task').get_user_blogs()
# print(s)
# s = UserMethods('https://api.tumblr.com','test-task').set_like_on_post(699547815757676544,'KxbBrfF9')
# print(s)
