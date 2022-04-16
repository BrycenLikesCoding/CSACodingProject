from deta import Deta
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

global detaInformation

detaInformation = {
    'key': 'b08vglli_XfZZkGogKbBZvzaGmr4xEAMqHTXLnrLA'
}

def initDeta():
	deta = Deta(detaInformation['key'])
	return deta

deta = initDeta()

users = deta.Base("users")
videos = deta.Base("videos")
thumbnails = deta.Drive("thumbnails")

thumbnails.put('test_thumbnail_1.jpg', path='./thumb_test')
