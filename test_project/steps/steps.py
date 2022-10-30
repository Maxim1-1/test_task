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

    def __init__(self, base_url):
        self.base_url = base_url

    def create_new_post_with_photo(self, photo_path=test_photo_path):
        post_methods = PostMethods(self.base_url, CONFIG["blog_id"])
        new_post = post_methods.create_post(type_message='photo', message=RANDOM_TEXT,
                                            picture_path=photo_path)
        post_id = JsonUtils().get_value_json(new_post["body"], value='id')
        return new_post["body"], post_id

    def is_validate_text(self):

    # assert new_post["status_code"] == 201, f"Статус код отличается от ожидаемого {new_post['status_code']}"
    # new_post_id = new_post["body"]["response"]["id"]
    # assert post_methods.get_post_info_by_id(new_post_id)["body"]["response"][
    #            'slug'] == RANDOM_TEXT, "Информация в новом посте не совпадает с отправленной"
    # link = post_methods.get_post_info_by_id(new_post_id)["body"]["response"]["content"][0]['media'][0]['url']
    # assert Steps().is_validate_picture_new_post(link_on_photo=link,
    #                                             photo_path=r'D:\test_task\test_project\test_data\test_img.jpg'), "Картинки не совпадают"
    # assert post_methods.delete_post(new_post_id)["status_code"] == 200, 'Новый пост не был удален'

    def is_validate_response_is_json_format(self, response):
        """checks that the response type is json"""
        return isinstance(response, dict)

    # @staticmethod
    # def is_validate_status_code(actual_status_code, expected_status_code):
    #     """compares the status code"""
    #     return actual_status_code == expected_status_code

    def is_validate_text_new_post(self, actual_text: str, expected_text: str):
        return actual_text == expected_text

    def is_validate_picture_new_post(self, link_on_photo, photo_path):
        """This method compares the photo with another photo that is located on the link"""
        project_photo = ApiUtils().get(link_on_photo, stream=True)
        image_one = Image.open(photo_path)
        image_two = Image.open(project_photo.raw)
        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox():
            return True
        else:
            return False


s = Steps().create_new_post_with_photo()

print(JsonUtils().get_value_json(s["body"], value='slug'))
