#https://filemagic.readthedocs.io/en/latest/guide.html
import magic

def file_on_path(filepath):
    with magic.Magic() as m:
        return m.id_filename(filepath)
    
def file_on_buffer(buffer):
    with magic.Magic() as m:
        return m.id_buffer(buffer)

def get_mime_type(filepath):
    with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
        return m.id_filename(filepath)

def get_encoding(filepath):
    with magic.Magic(flags=magic.MAGIC_MIME_ENCODING) as m:
        return m.id_filename(filepath)

