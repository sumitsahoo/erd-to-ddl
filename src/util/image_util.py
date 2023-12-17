import base64

from src.util.log_util import LogUtil


class ImageUtil:
    def __init__(self):
        self.log = LogUtil()

    def generate_data_url(self, image_path):
        # Generate data URL from image path
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            data_url = "data:image/jpeg;base64," + encoded_string.decode("utf-8")
            return data_url
