def index_map(urlID):

    import requests as req

    url_or = 'https://a.gusc.cartocdn.com/liquidaciones/api/v1/map/liquidaciones@7d13fb84@6bb560cb9ac70300b0009d5a5092fc6d:1650976279569/2/attributes/'

    url=url_or+str(urlID)

    contenido=req.get(url)

    if 'errors' not in contenido.text:
        return (contenido.text)
    else: 
        pass