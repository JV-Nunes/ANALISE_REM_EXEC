import requests

class GetData:
    def __init__(self, url):
        self.url = url
    
    def get_data(self):
        '''Realiza o download e grava um arquivo csv a partir de uma página da internet'''
        response = requests.get(self.url)

        with open('data/serie_historica.csv', 'wb') as file:
            file.write(response.content)
    