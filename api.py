from fastapi import APIRouter

import db_connection

router = APIRouter(
    prefix="/api"
)


@router.post("/add/url")
async def add_url(url):
    print(url)
    db_connection.insert_data(url)
    return {"url": url}
