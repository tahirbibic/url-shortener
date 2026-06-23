import models

class UrlRepository:
    def get_by_original(self, db, original_url):
        return db.query(models.Url).filter(models.Url.original_url == original_url).first()

    def get_by_code(self, db, short_code):
        return db.query(models.Url).filter(models.Url.short_code == short_code).first()

    def create(self, db, short_code, original_url):
        new_url = models.Url(short_code=short_code, original_url=original_url)
        db.add(new_url)
        db.commit()
        db.refresh(new_url)
        return new_url