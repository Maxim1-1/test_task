from test_project.project_utils.parser_utils import UtilsParse
from requests_oauthlib import OAuth1

CONFIG = UtilsParse().parse_config()


class AuthorizationUtils:


    def get_auth(self):
        oauth = OAuth1(CONFIG["client_key"], client_secret=CONFIG["client_secret"],
                       resource_owner_key=CONFIG["resource_owner_key"],
                       resource_owner_secret=CONFIG["resource_owner_secret"])
        return oauth
