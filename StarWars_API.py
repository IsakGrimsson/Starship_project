import requests

#class to fetch data from API and return array of dictionaries
class StarWarsAPI:
    #fetch one specific page number
    def fetch_page(self, collection: str, page: int):
        page_request = requests.session().get(f"https://swapi.dev/api/{collection}/?page={page}")
        return page_request.json()["results"]
    #fetch the first x number of pages
    def fetch_num_pages(self, collection: str, num_of_pages: int):
        all_pages = []
        for page in list(range(1,num_of_pages+1)):
            each_page = self.fetch_page(collection, page)
            all_pages.extend(each_page)
        return all_pages
    #fetch all of the pages for specified collection
    def fetch_all_pages(self, collection: str):
        all_pages = []
        page = 1
        while True:
            page_request = requests.get(f"https://swapi.dev/api/{collection}/?page={page}")
            # added .get so that when there is no response it will recover
            page_data = page_request.json().get("results", [])
            # break when there is no more data
            if not page_data:
                break
            all_pages.extend(page_data)
            page += 1
        return all_pages

    def replace_url(self, list_of_dicts, inner, retrieve):
        for dict in list_of_dicts:
            url_replaced_with_retrieve = []
            for url in dict[inner]:
                url_json = requests.session().get(url).json()
                retrieve_element = url_json[retrieve]
                url_replaced_with_retrieve.append(retrieve_element)
            dict[inner] = url_replaced_with_retrieve
        return list_of_dicts