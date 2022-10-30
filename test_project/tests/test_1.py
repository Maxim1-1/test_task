import pytest
from test_project.project_utils.parser_utils import UtilsParse
from test_project.project_api_methods.posts_methods import PostMethods
from test_project.project_api_methods.user_methods import UserMethods
from test_project.project_utils.random_text_utils import RandomUtils
from test_project.steps.steps import Steps
from test_project.project_utils.parse_json_utils import JsonUtils

RANDOM_TEXT = RandomUtils().get_random_text(5)
CONFIG = UtilsParse().parse_config()
TEST_DATA = UtilsParse().parse_test_data()
EDIT_TEXT = RandomUtils().get_random_text(5)

class TestsTumblr:

    def test_1_user_case(self, add_url):
        base_url = 'https://api.tumblr.com'
        post_methods = PostMethods('https://api.tumblr.com', CONFIG["blog_id"])
        user_methods = UserMethods('https://api.tumblr.com', CONFIG["blog_id"])
        new_post = Steps(base_url).create_new_post_with_photo(message=RANDOM_TEXT)
        assert new_post["status_code"] == 201, f"Статус код отличается от ожидаемого"
        new_post_id = JsonUtils().get_value_json(new_post["body"], value='id')
        assert Steps(base_url).get_text_post(new_post_id,obj_find='slug') == RANDOM_TEXT, "Информация в новом посте не совпадает с отправленной"
        link = Steps(base_url).get_link_on_photo_from_post(new_post_id)
        assert Steps().is_validate_picture_new_post(link_on_photo=link), "Картинки не совпадают"
        reblog_key = Steps(base_url).get_text_post(new_post_id, "reblog_key")
        assert user_methods.set_like_on_post(reblog_key=reblog_key, post_id=new_post_id)["status_code"] == 200, "Статус код не совпадает с ожидаемым"
        assert post_methods.get_post_info_by_id(new_post_id)["body"]["response"]["liked"], "Лайк на пост не поставлен"

        assert post_methods.delete_post(new_post_id)["status_code"] == 200, 'Новый пост не был удален'

    @pytest.mark.parametrize("lenght_post_id", [17, 18, 19])
    def test_2_checking_non_existent_post(self, add_url, lenght_post_id):
        base_url = 'https://api.tumblr.com'
        random_number = RandomUtils().get_random_number(lenght_post_id)
        post = PostMethods(base_url, CONFIG["blog_id"])
        new_post = post.get_post_info_by_id(random_number)
        assert new_post["status_code"] == 404, "Код ошибки не 404"
        assert Steps(base_url).is_validate_response_is_json_format(new_post)
        assert post.get_post_info_by_id(random_number)['msg'] == TEST_DATA["expected_msg_404"], "Сообщение об ошибке не совпадает с ожидаемым"

    def test_3_checking_reblog(self):
        base_url = 'https://api.tumblr.com'
        post = PostMethods('https://api.tumblr.com', CONFIG["blog_id"])
        reblog_key = Steps(base_url).get_text_post(TEST_DATA["test_post_id"],"reblog_key")
        assert post.post_reblog(reblog_key=reblog_key, post_id=TEST_DATA["test_post_id"],comment=RANDOM_TEXT)["status_code"] == 201, "Статус код не соответствует ожидаемому"

    def test_4_user_case(self):
        base_url = 'https://api.tumblr.com'
        post_methods = PostMethods('https://api.tumblr.com', CONFIG["blog_id"])
        new_post = Steps(base_url).create_new_post(message=RANDOM_TEXT,title=RANDOM_TEXT)
        assert new_post["status_code"] == 201, f"Статус код отличается от ожидаемого"
        new_post_id = JsonUtils().get_value_json(new_post["body"], value='id')
        assert Steps(base_url).get_text_post(new_post_id,"slug") == RANDOM_TEXT, "Информация в новом посте не совпадает с отправленной"
        assert post_methods.edit_text_post(post_id=new_post_id, comment=EDIT_TEXT)["status_code"] == 200, "Статус код не соответствует ожидаемому"
        assert Steps(base_url).get_edit_text(new_post_id) == EDIT_TEXT, "Новый текст поста не совпадает с отправленным"

    def test_5_cheking_following_user(self):
        base_url = 'https://api.tumblr.com'
        user_methods = UserMethods('https://api.tumblr.com', CONFIG["blog_id"])
        assert user_methods.get_user_blogs()["status_code"] == 200, "Статус код не совпадает с ожидаемым"
        assert Steps(base_url).get_user_blogs() == TEST_DATA["following_blog"], "Тестовый блог отсутствует в списке"
