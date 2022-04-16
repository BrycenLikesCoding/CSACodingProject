from deta import Deta
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

global detaInformation

detaInformation = {
    'key': 'b08vglli_XfZZkGogKbBZvzaGmr4xEAMqHTXLnrLA'
}


deta = Deta(detaInformation['key'])

users = deta.Base("users")
videos = deta.Base("videos")
thumbnails = deta.Drive("thumbnails")

thumbnails.put('test_thumbnail_1.jpg', path=r'C:\Users\CSA9876\PycharmProjects\CSACodingProject\test_thumbnail_1.jpg')

@app.get('/', response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
<HTML>
	<HEAD>
	    <title>
	        not youtube
	    </title>
	    
	    <link href="https://www.youtube.com/favicon.ico" rel='icon'>
	    <link href="https://www.youtube.com/favicon.ico" rel='shortcut icon'>
	    
	    <link href="https://turbine1k.repl.co/cdn/burning.css" rel='stylesheet'>
	    
	    <style>
	        html {
	            padding:5px;
	        }
	        .links {
	            /*float:right;*/
	            border:solid;
	            border-width:3px;
	            padding:5px;
	            position:absolute;
	            
	            
	        }
	        .line2 {
	            width:100%;
	            background:white;
	            padding:1px;
	        }
	    </style>
	</HEAD>
	<BODY>
		<h1>
		    not youtube
		</h1>
		<marquee width="200">
		    <b>
		        <i>
		            now with pretzels!
		        </i>
		    </b>
		</marquee>
		<div class="links">
		    <a href="/upload">upload a video</a>
		</div>
		<div class="line2"></div>
		<div id="videos"></div>
	</BODY>
</HTML>"""

@app.get('/upload', response_class=HTMLResponse)
def root():
    return "Hello, World!"

if __name__ == "__main__":
    import uvicorn