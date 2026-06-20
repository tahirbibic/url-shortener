from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import random
import string

from database import engine, get_db, Base
import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


def generate_code(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


@app.post("/shorten", response_model=schemas.CreateResponse)
def shorten(request: schemas.CreateRequest, db: Session = Depends(get_db)):
    existing = db.query(models.Url).filter(models.Url.original_url == request.original_url).first()
    if existing:
        return existing
    code = generate_code()
    new_url = models.Url(short_code=code, original_url=request.original_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url


@app.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):
    url = db.query(models.Url).filter(models.Url.short_code == short_code).first()
    if url is None:
        raise HTTPException(status_code=404, detail="Not found")
    return RedirectResponse(url=url.original_url)