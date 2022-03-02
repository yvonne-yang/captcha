import argparse
from captcha.image import ImageCaptcha
from tqdm import tqdm
import os

imageCaptcha = ImageCaptcha()


def run():
    """Run the generator with arguments:
    eg. python gen_char_images.py 100 --width=20 --height=75 --dst="trial"
    """
    parser = argparse.ArgumentParser(
        description="Generate single-character images from a captcha."
    )
    parser.add_argument(
        "n", type=int, help="number of images to generate for each character"
    )
    parser.add_argument(
        "-d", "--dry-run", action="store_true", help="run without saving images"
    )
    parser.add_argument(
        "-w", "--width", type=int, default=34, help="image width in pixels"
    )
    parser.add_argument(
        "--dst",
        type=str,
        default="chars",
        help="destination folder (see README for folder structure)",
    )
    parser.add_argument("--height", type=int, default=75, help="image height in pixels")
    parser.add_argument(
        "-c",
        "--chars",
        type=str,
        default="0123456789abcdefghijklmnopqrstuvwxyz",
        help='characters to generate image for (eg. "adf")',
    )

    args = parser.parse_args()

    for i in tqdm(range(args.n)):
        imageCaptcha.generate_char_image(
            args.chars,
            dst=args.dst,
            wid=args.width,
            height=args.height,
            dry_run=args.dry_run,
        )


def captcha_samples():
    imageCaptcha.write("1a2b6", f"images/1a2b6.png")
    imageCaptcha.write("cdegh", f"images/cdegh.png")
    imageCaptcha.write("opqrstu", f"images/opqrstu.png")

    img = imageCaptcha.generate_image("12m5f")
    img.show()


if __name__ == "__main__":
    run()
