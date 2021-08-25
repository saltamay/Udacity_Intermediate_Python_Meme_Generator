# Udacity Intermediate Python Nanodegree

## Project #2: Meme_Generator

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Overview

The application must be able to perform the following:

- Interact with a variety of complex filetypes. 
- Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
- Load, manipulate, and save images.
- Accept dynamic user input through a command-line tool and a web service.


## Usage

### CLI app

```
usage: python meme.py [-h] [--body BODY] [--author AUTHOR] [--path PATH]

optional arguments:
  -h, --help       show this help message and exit
  --body BODY      text that want to show
  --author AUTHOR  author of the text
  --path PATH      file path for background image you want
```

### Web app

```
python app.py
```

The server runs on http://127.0.0.1:5000/

## Modules

- **QuoteEngine:** The Quote Engine module is responsible for ingesting many types of files that contain quotes. 

- **IngestorInterface:** An abstract base class, IngestorInterface defines two methods `can_ingest` and `parse` which is extended by the subclasses (**CSVIngestor, TXTIngestor, PDFIngestor, DocxIngestor**) created by using **strategy object pattern**.

- **Ingestor class:** realizes abstract `IngestorInterface` and encapsulates the helper strategy classes.

- **MemeEngine:** The Meme Engine Module is responsible for manipulating and drawing text onto images.

## Dependencies

`requirements.txt`contains the complete list of python dependencies used. Main dependencies include:

* pandas
* flask
* requests

## Feature Improvements

- Make it Unique. Add your own content (images and quotes).
- Unit test everything. Define unit tests to ensure your code functions as intended.
- Deploy as a Webapp. Deploy the flask server to Heroku so that it can be accessed publicly.
- Extend your system. Be creative by using your meme generator in unique ways – ideas include:
- Sharing the generated image with an email
- Using a 3rd party API to dynamically add more information. You can check out a bunch of 3rd party APIs 
  [here](https://apilist.fun/). 
  Some possibilities are:
  - Weather, traffic, locations
  - Use Amazon Rekognition to identify the image content and define rules to choose the quote category


