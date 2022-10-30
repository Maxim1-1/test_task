from PIL import Image
from PIL import ImageChops
from base.api_utils import ApiUtils


class Steps:

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

# s = Steps().is_validate_picture_new_post()
# print(s)
