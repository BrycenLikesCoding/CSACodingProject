from deta import Deta
from fastapi import FastAPI, Request, Response, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, StreamingResponse
import secrets

app = FastAPI()


detaInformation = {
    'key': 'b08vglli_XfZZkGogKbBZvzaGmr4xEAMqHTXLnrLA'
}


deta = Deta(detaInformation['key'])

videos = deta.Drive("videos")
thumbnails = deta.Drive("thumbnails")

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/upload', response_class=HTMLResponse)
def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post('/videos/upload', response_class=HTMLResponse)
async def upload(request: Request, title: str = Form(...), creator: str = Form(...), video_file: UploadFile = File(...), thumbnail: UploadFile = File(...)):
    print(title, creator)
    print(video_file, thumbnail)

    k = secrets.token_urlsafe(16)
    print(k)
    vf = k + ".mp4"
    tf = k + ".png"
    videos.put(vf, video_file.file)
    thumbnails.put(tf, thumbnail.file)
    return templates.TemplateResponse("success.html", {"request": request, "title": title, "creator": creator})

@app.get('/img/{key}', response_class=StreamingResponse)
def get_thumbnails(key: str):
    name = key + ".png"
    x = thumbnails.get(name)
    return StreamingResponse(x.iter_chunks(1024), media_type="image/png")

@app.get('/videos/watch/{key}', response_class=StreamingResponse)
def video_get(key: str):
    name = key + '.mp4'
    x = videos.get(name)
    return StreamingResponse(x.iter_chunks(1024), media_type="video/mp4")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", reload=True)