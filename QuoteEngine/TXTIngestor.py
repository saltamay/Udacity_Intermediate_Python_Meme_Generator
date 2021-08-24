from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse a txt file that contains quotes and authors

        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            List[QuoteModel] -- list of quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(path, 'r') as reader:
            for line in reader:
                if line != "":
                    parse = [word.strip() for word in line.split('-')]
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        return quotes
