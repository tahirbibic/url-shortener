from fastapi import HTTPException, Request
from cache import r

RATE_LIMIT = 100
WINDOW = 60

def check_rate_limit(request: Request):
    ip = request.client.host
    key = f"rate:{ip}" 

    count = r.incr(key)

    if count ==1:
        r.expire(key, WINDOW)

    if count > RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests")