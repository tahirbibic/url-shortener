import random
import string
from repository import UrlRepository
from cache import r

repo = UrlRepository()

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))

class UrlService:
    def shorten(self, db, original_url):
        existing = repo.get_by_original(db, original_url)
        if existing:
            return existing
        code = generate_code()
        return repo.create(db, code, original_url)

    def get_original(self, db, short_code):
        cached = r.get(short_code)
        if cached:
            return cached

        url = repo.get_by_code(db, short_code)
        if url is None:
            return None

        r.set(short_code, url.original_url, ex=3600)
        return url.original_url