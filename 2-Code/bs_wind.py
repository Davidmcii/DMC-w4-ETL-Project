def bs_wind(urlID):

    import requests as req
    from bs4 import BeautifulSoup as bs

    url_or = 'https://www.thewindpower.net/windfarm_en_'
    url_fin='.php'
    url_wind=url_or+str(urlID)+url_fin

    html=req.get(url_wind).text

    soup=bs(html, 'html.parser')
    tarjetas=soup.find_all('li', class_='puce_texte')
    fila=[el.text for el in tarjetas]
    return fila

