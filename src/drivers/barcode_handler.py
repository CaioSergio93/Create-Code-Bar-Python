from barcode import Code128
from barcode.writer import ImageWriter

class BarcodeHandle:
    def create_barcode(self, product_code: str) ->  str:
        tag = Code128(product_code, writer=ImageWriter())
        path_from_tag = f'{tag}'
        tag.save(path_from_tag)

        return path_from_tag