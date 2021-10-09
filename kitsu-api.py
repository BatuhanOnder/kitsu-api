import requests
import json
from requests.auth import HTTPBasicAuth
# httpx library


class API:
    # base_url = "https://kitsu.io/api/edge/"

    def __init__(self, base_url, client_id, client_secret):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        

    def search(self, search_type, filter, search_text, limit = 20, offset = 0):
        url = f"{search_type}?filter[{filter}]={search_text}"
      
        url += f"{self.base_url}anime?page[limit]={limit}&page[offset]={offset}"
        
        url = self.base_url + url

        r = requests.get(url)
        with open(f"{search_type}-{search_text}-{filter}-{offset}-{offset+limit}.txt", "a") as file:
            json.dump(r.json(), file, indent=4)

    def authentication(self):   
        url = "https://kitsu.io/api/oauth"

    #     # Send Header
    #     # api_key = "sadsadasd"
    #     # header = {"auth: Bareer %s" % (api_key)}
    #     # r = requests.post(url, header=header)
    
        header = {"Content-Type : application/json"}
        r = requests.post(url, header = header)
        print(r.status_code)

 
    # indent bosluğu, r.text response cevabını ve de file dosyayı belirtir.
    # string builder olarak %s ekleyim sonta %() seklinde eklenebilir , veya f"" seklinde yazıp eklenmek istenen parameter
    # {} icerisine import edilebilr

  
  
# sort eksik
if __name__ == "__main__":
    q = API("https://kitsu.io/api/edge/","dd031b32d2f56c990b1425efe6c42ad847e7fe3ab46bf1299f05ecd856bdb7dd0","54d7307928f63414defd96399fc31ba847961ceaecef3a5fd93144e960c0e151")
    # q.search("anime", "categories", "adventures")
    q.authentication()

