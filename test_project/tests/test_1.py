import pytest
from test_project.project_utils.parser_utils import UtilsParse
from test_project.project_api_methods.posts_methods import PostMethods
from test_project.project_api_methods.user_methods import UserMethods
from test_project.project_utils.random_text_utils import RandomUtils
from test_project.steps.steps import Steps


RANDOM_TEXT = RandomUtils().get_random_text(5)
CONFIG = UtilsParse().parse_config()
TEST_DATA = UtilsParse().parse_test_data()


class TestsTumblr:

    # RANDOM_TEXT = RandomUtils().get_random_text(5)
    EDIT_TEXT = RandomUtils().get_random_text(5)


    def test_1_user_case(self,add_url):
        new_post = Steps(add_url["url"]).create_new_post_with_photo()
        # post_methods = PostMethods('https://api.tumblr.com', CONFIG["blog_id"])
        # new_post = post_methods.create_post(type_message='photo', message=RANDOM_TEXT, picture_path=r'D:\test_task\test_project\test_data\test_img.jpg')
        assert new_post["status_code"] == 201, f"Статус код отличается от ожидаемого"
        new_post_id = new_post["body"]["response"]["id"]
        assert post_methods.get_post_info_by_id(new_post_id)["body"]["response"]['slug'] == RANDOM_TEXT, "Информация в новом посте не совпадает с отправленной"
        link = post_methods.get_post_info_by_id(new_post_id)["body"]["response"]["content"][0]['media'][0]['url']
        assert Steps().is_validate_picture_new_post(link_on_photo=link,photo_path=r'D:\test_task\test_project\test_data\test_img.jpg'),"Картинки не совпадают"
        assert post_methods.delete_post(new_post_id)["status_code"] == 200, 'Новый пост не был удален'


    @pytest.mark.parametrize("lenght_post_id", [(17), (18), (19)])
    def test_2_checking_non_existent_post(self, add_url, lenght_post_id):
        random_number = RandomUtils().get_random_number(lenght_post_id)
        post_methods = PostMethods('https://api.tumblr.com', CONFIG["blog_id"])
        assert post_methods.get_post_info_by_id(random_number)["status_code"] == 404, "Код ошибки не 404"
        assert post_methods.get_post_info_by_id(random_number)["body"]["meta"]["msg"] == TEST_DATA[
            "expected_msg_404"], "Сообщение об ошибке не совпадает с ожидаемым"

    def test_3_checking_reblog(self):
        post = PostMethods('https://api.tumblr.com', CONFIG["blog_id"])
        reblog_key = post.get_post_info_by_id(TEST_DATA["test_post_id"])["body"]["response"]["reblog_key"]
        assert post.post_reblog(reblog_key=reblog_key, post_id=TEST_DATA["test_post_id"],
                                comment=RANDOM_TEXT)["status_code"] == 201, "Статус код не соответствует ожидаемому"

    def test_4_user_case(self):
        post_methods = PostMethods('https://api.tumblr.com', CONFIG["blog_id"])
        user_methods = UserMethods('https://api.tumblr.com', CONFIG["blog_id"])
        new_post = post_methods.create_post(type_message='text', message=RANDOM_TEXT)
        assert new_post["status_code"] == 201, f"Статус код отличается от ожидаемого {new_post['status_code']}"
        new_post_id = new_post["body"]["response"]["id"]
        assert post_methods.get_post_info_by_id(new_post_id)["body"]["response"][
                   'slug'] == RANDOM_TEXT, "Информация в новом посте не совпадает с отправленной"
        assert post_methods.edit_text_post(post_id=new_post_id,comment=self.EDIT_TEXT)["status_code"] == 200,"Статус код не соответствует ожидаемому"
        assert post_methods.get_post_info_by_id(new_post_id)["body"]["response"]['slug'] == self.EDIT_TEXT, "Новый текст поста не совпадает с отправленным"
        reblog_key = post_methods.get_post_info_by_id(new_post_id)["body"]["response"]["reblog_key"]
        assert user_methods.set_like_on_post(reblog_key=reblog_key, post_id=new_post_id)["status_code"] == 200,"Статус код не совпадает с ожидаемым"
        assert post_methods.get_post_info_by_id(new_post_id)["body"]["response"]["liked"],"Лайк на пост не поставлен"

    def test_5_cheking_following_user(self):
        user_methods = UserMethods('https://api.tumblr.com', CONFIG["blog_id"])
        assert user_methods.get_user_blogs()["status_code"] == 200, "Статус код не совпадает с ожидаемым"
        assert user_methods.get_user_blogs()["body"]["response"]["blogs"][0]["name"] == TEST_DATA[
            "following_blog"], "Тестовый блог отсутствует в списке"
