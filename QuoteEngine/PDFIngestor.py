from typing import List
import subprocess
import random
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse a pdf file that contains quotes and authors

        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            List[QuoteModel] -- list of quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        temp = f'./tmp/{random.randint(0, 1000000)}.txt'
        call = subprocess.run(['pdftotext', path, temp])

        quotes = []

        with open(temp, 'r') as reader:
            for line in reader.readlines():
                line = line.strip('\n\r')
                if len(line) > 0:
                    parsed = [word.strip() for word in line.split('-')]
                    new_quote = QuoteModel(parsed[0], parsed[1])
                    quotes.append(new_quote)

        os.remove(temp)

        return quotes
