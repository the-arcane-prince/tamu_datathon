from .wikipedia import WikipediaApi

def test_wikipedia_api():
    api = WikipediaApi()
    print(api.handle_query("python"))