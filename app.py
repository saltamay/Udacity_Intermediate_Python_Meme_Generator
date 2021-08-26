import random
import os
import requests
from flask import Flask, render_template, request

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for file_path in quote_files:
        try:
            quotes = quotes + Ingestor.parse(file_path)
        except FileNotFoundError:
            print(f'Uh oh, something went wrong - {file_path}')
        except TypeError:
            print(f"Invalid file type '{file_path}'. Please try again.")

    images_path = "_data/photos/dog/"

    imgs = [
        os.path.join(
            images_path,
            file) for file in os.listdir(images_path) if os.path.isfile(
            os.path.join(
                images_path,
                file))]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = imgs[random.randint(0, len(imgs) - 1)]
    quote = quotes[random.randint(0, len(quotes) - 1)]
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form.get("image_url")
    quote_body = request.form.get("body")
    quote_author = request.form.get("author")

    try:
        if not os.path.isdir('./tmp'):
            os.makedirs('./tmp')

        temp = f'./tmp/{random.randint(0, 1000000)}.jpg'
        image_request = requests.get(image_url, stream=True)

        if image_request.status_code == 200:
            with open(temp, 'wb') as file:
                file.write(image_request.content)

            path = meme.make_meme(temp, quote_body, quote_author)

            os.remove(temp)

            return render_template('meme.html', path=path)
    except BaseException:
        return render_template(
            'meme_form.html',
            error="Uh oh! Something went wrong, please try again.")


if __name__ == "__main__":
    app.run()
