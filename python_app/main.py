import logging
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pytz import timezone

logging.basicConfig(filename="/var/log/python_app.log", level=logging.DEBUG)

time_format = fmt = "%H:%M:%S"
moscow_timezone = "Europe/Moscow"

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    logging.info("Processing 'GET' request for route '/'")
    moscow_local_time = datetime.now(timezone(moscow_timezone))

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "moscow_time": moscow_local_time.strftime(time_format)},
    )
