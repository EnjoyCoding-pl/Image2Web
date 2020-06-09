from PIL import Image

class ImageConverter:
    def __init__(self, size):
        self.size = size

    def open_image(self, path):
        img = Image.open(path)
        img.convert("RGB")
        return img
        
    def resize(self, image):
        return image.thumbnail((self.size, self.size))