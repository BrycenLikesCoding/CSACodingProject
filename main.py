from deta import Deta
from fastapi import FastAPI, Request, Response, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI()


detaInformation = {
    'key': 'b08vglli_XfZZkGogKbBZvzaGmr4xEAMqHTXLnrLA'
}


deta = Deta(detaInformation['key'])

users = deta.Base("users")
videos = deta.Base("videos")
thumbnails = deta.Drive("thumbnails")

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/upload', response_class=HTMLResponse)
def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post('/videos/upload', response_class=HTMLResponse)
def upload(request: Request, title: str = Form(...), creator: str = Form(...), video_file: UploadFile = File(...),
           thumbnail: UploadFile = File(...)):
    print(title, creator)
    print(video_file, thumbnail)
    return templates.TemplateResponse("success.html", {"request": request, "title": title, "creator": creator})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", reload=True)