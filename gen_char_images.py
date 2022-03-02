from tqdm import tqdm
from captcha.image import ImageCaptcha
import os

# Make sure you have folders a-z and 0-9 created in dst first
# (mkdir dst/{a..z} dst/{0..9})
imageCaptcha = ImageCaptcha()
for i in tqdm(range(190)):
    imageCaptcha.generate_char_image(
        "0123456789abcdefghijklmnopqrstuvwxyz", dst="chars"
    )
# imageCaptcha.write("1a2b6", f"images/{count}/1a2b6.png")
# imageCaptcha.write("cdegh", f"images/{count}/cdegh.png")
# imageCaptcha.write("opqrstu", f"images/{count}/opqrstu.png")

# img = imageCaptcha.generate_image("12m5f")
# img.show()
