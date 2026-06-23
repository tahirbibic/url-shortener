from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models, schemas
from service import UrlService
from rate_limit import check_rate_limit

Base.metadata.create_all(bind=engine)
app = FastAPI()
service = UrlService()

@app.post("/shorten", response_model=schemas.CreateResponse)
def shorten(request: schemas.CreateRequest, http_request: Request, db: Session = Depends(get_db)):
    check_rate_limit(http_request)
    return service.shorten(db, request.original_url)

@app.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):
    original = service.get_original(db, short_code)
    if original is None:
        raise HTTPException(status_code=404, detail="Not found")
    return RedirectResponse(url=original)