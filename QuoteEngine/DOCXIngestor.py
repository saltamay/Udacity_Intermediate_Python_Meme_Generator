from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse a docx file that contains quotes and authors

        Arguments:
            path {str} -- the file location for the input file.
        Returns:
            List[QuoteModel] -- list of quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = [word.strip() for word in para.text.split('-')]
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
