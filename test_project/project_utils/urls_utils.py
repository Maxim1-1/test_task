from test_project.project_utils.parser_utils import UtilsParse


CONFIG = UtilsParse().parse_config()

class UrlsUtils:
    def create_url_for_request(self, obj_request, endpoint, base_url, blog_id, post_id=None):

        if obj_request == 'user':
            url_user = f"{base_url}/{CONFIG['ver_api']}/{CONFIG['resource_user']}{endpoint}"

            return url_user
        elif obj_request == 'post':

            url_post = f"{base_url}/{CONFIG['ver_api']}/{CONFIG['resource_post']}/{blog_id}{endpoint}"

            if post_id is None:

                return url_post
            else:
                url_post_id = f"{url_post}/{post_id}"

                return url_post_id

