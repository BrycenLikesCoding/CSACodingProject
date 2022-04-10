from deta import Deta
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

global detaInformation

detaInformation = {
    'key': 'b08vglli_aRZbmhfWKATs54djaSHiZrFu2cFqJn19',
    'id': 'b08vglli'
}

def initDeta():
	deta = Deta(detaInformation['key'])
	return deta

deta = initDeta()

users = deta.Base("users")
videos = deta.Base("videos")
thumbnails = deta.Drive("thumbnails")

thumbnails.put('test_thumbnail_1.jpg', path='./thumb_test')
