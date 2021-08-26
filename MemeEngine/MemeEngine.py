import textwrap
import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:

    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir

    def make_meme(
            self,
            img_path: str,
            text: str,
            author: str,
            width=500) -> str:
        """Create a meme with a caption

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- text for caption's body.
            author {str} -- text for caption's author
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(img_path)

        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))

        img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            wrapper = textwrap.TextWrapper(width=30)
            draw = ImageDraw.Draw(img)
            font_body = ImageFont.truetype(
                './fonts/LilitaOne-Regular.ttf', size=32)
            font_author = ImageFont.truetype(
                './fonts/LilitaOne-Regular.ttf', size=20)
            top = random.randint(height / 4, 3 * height / 4)
            left = random.randint(10, 30)

            for word in wrapper.wrap(text=text):
                top = top + font_body.size
                draw.text((left, top), word,
                          font=font_body,
                          fill='black', stroke_width=1, stroke_fill='white')
            draw.text((left + 10, top + font_body.size), f'- {author}',
                      font=font_author,
                      fill='black', stroke_width=1, stroke_fill='white')

        img_name = f'{random.randint(0, 1000000)}.jpg'
        output_path = f'{self.output_dir}/{img_name}'
        img.save(output_path)

        return output_path
