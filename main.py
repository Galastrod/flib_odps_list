import uvicorn
import requests
from fastapi import FastAPI
from fastapi import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import requests
import xml.etree.ElementTree as Xml

from www.server import __flibusta_url, collectionParse, search, getColection, getNewBoks

app = FastAPI()
app.mount( '/assets/',  StaticFiles( directory="assets" ), name="assets")
templates = Jinja2Templates( directory="templates" )

@app.get( '/' )
def home( request: Request ) :
	return templates.TemplateResponse( 
		'index.html',
		{
			'request': request,
			'app_name': "Flibusta OPDS API"
		}
	)
	
@app.get( '/new' )
def home() :
	return getNewBoks()
	
if __name__ == "__main__" :
	uvicorn.run( "main:app", host="0.0.0.0", port=8080, reload=True)
