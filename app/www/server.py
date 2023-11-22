################################################################
# module Constants
import requests
import xml.etree.ElementTree as Xml

__flibusta_url 	= 'http://flibusta.site'
# module Constants end
################################################################

################################################################
# module Request parser
# The module parse request xml from flibusta to object data
def linksProcess( links ) :
	res = {}
	for link in links :
		
		if '/opds/author/' in link.attrib['href'] :
			res['author_link'] = link.attrib['href']
			
		if '/opds/sequencebooks/' in link.attrib['href'] :
			res['sequence_link'] = link.attrib['href']
			
		if link.attrib['type'] == 'application/fb2+zip' :
			res['download_fb2'] = link.attrib['href']
			
		if link.attrib['type'] == 'application/epub+zip' :
			res['download_epub'] = link.attrib['href']
			
		if link.attrib['type'] == 'application/x-mobipocket-ebook' :
			res['download_mobi'] = link.attrib['href']
		
	return res

def collectionParse( xml_text ) :
	__atom 	= '{http://www.w3.org/2005/Atom}'
	__os	= '{http://a9.com/-/spec/opensearch/1.1/}'
	
	res     = {}
	books   = []
	root    = Xml.fromstring( xml_text )

	res['start_index']		= root.find( __os + 'startIndex' ).text
	res['total_result'] 	= root.find( __os + 'totalResults' ).text
	res['items_per_page'] 	= root.find( __os + 'itemsPerPage' ).text
	
	for entry in root.iter( __atom + 'entry' ) : 
		book = {}
		
		book['links'] 		= linksProcess( entry.findall( __atom + 'link' ) )
		book['title'] 		= entry.find( __atom + 'title' ).text
		book['author'] 		= entry.find( __atom + 'author//' ).text
		 
		books.append( book )
	
	res['books'] = books
	
	return res
# module Request parser end.
################################################################

################################################################
# module Get source from flibusta
def search( req ) :
	response 	= requests.get( f'{__flibusta_url}/opds/opensearch?searchTerm={req}' )
	books		= collectionParse( response.text )
	return books

def getColection( url ) :
	response 	= requests( f'{__flibusta_url}{url}' ) 
	books 		= collectionParse( response.text )
	drawColection( books )
	
def getNewBoks() :
	response 	= request( f'{__flibusta_url}/opds/new/0/new' )
	books 		= collectionParse( response.text )
	return books
# module Get source from flibusta end
################################################################
	