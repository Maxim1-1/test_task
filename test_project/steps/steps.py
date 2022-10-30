from PIL import Image
from PIL import ImageChops
from base.api_utils import ApiUtils
from test_project.project_utils.parser_utils import UtilsParse
from test_project.project_api_methods.posts_methods import PostMethods
from test_project.project_api_methods.user_methods import UserMethods
from test_project.project_utils.random_text_utils import RandomUtils
from pathlib import Path
from test_project.project_utils.parse_json_utils import JsonUtils

RANDOM_TEXT = RandomUtils().get_random_text(5)
CONFIG = UtilsParse().parse_config()
TEST_DATA = UtilsParse().parse_test_data()
PHOTO_PATH = UtilsParse().parse_test_data()


class Steps:
    test_photo_path = Path(PHOTO_PATH["photo_path"])

    def __init__(self, base_url=None):
        self.base_url = base_url

    def create_new_post_with_photo(self, message, photo_path=test_photo_path, ):
        post_methods = PostMethods(self.base_url, CONFIG["blog_id"])
        new_post = post_methods.create_post(type_message='photo', message=message,
                                            picture_path=photo_path)
        return new_post

    def create_new_post(self, message, title):
        post_methods = PostMethods(self.base_url, CONFIG["blog_id"])
        new_post = post_methods.create_post(type_message='text', message=message, title=title)
        return new_post

    def get_text_post(self, post_id, obj_find=None):
        post_methods = PostMethods(self.base_url, CONFIG["blog_id"])
        post = post_methods.get_post_info_by_id(post_id)["body"]

        return JsonUtils().get_value_json(post, obj_find)

    def get_edit_text(self, post_id):
        post_methods = PostMethods(self.base_url, CONFIG["blog_id"])
        post = post_methods.get_post_info_by_id(post_id)["body"]
        return post["response"]["content"][-1]["text"]

    def get_link_on_photo_from_post(self, post_id):
        post_methods = PostMethods(self.base_url, CONFIG["blog_id"])
        return post_methods.get_post_info_by_id(post_id)["body"]["response"]["content"][0]['media'][0]['url']

    def is_validate_response_is_json_format(self, response):
        """checks that the response type is json"""
        return isinstance(response, dict)

    def get_user_blogs(self):
        user = UserMethods(self.base_url, CONFIG["blog_id"]).get_user_blogs()["body"]
        return JsonUtils().get_value_json(user,"name")

    def is_validate_text_new_post(self, actual_text: str, expected_text: str):
        return actual_text == expected_text

    def is_validate_picture_new_post(self, link_on_photo, photo_path=test_photo_path):
        """This method compares the photo with another photo that is located on the link"""
        project_photo = ApiUtils().get(link_on_photo, stream=True)
        image_one = Image.open(photo_path)
        image_two = Image.open(project_photo.raw)
        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox():
            return True
        else:
            return False

