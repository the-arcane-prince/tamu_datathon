import requests
from bs4 import BeautifulSoup
import json

# Function to scrape JSON data from a script tag with id "__NEXT_DATA__"
def scrape_next_data(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the <script> tag with id="__NEXT_DATA__" and type="application/json"
        script_tag = soup.find("script", {"id": "__NEXT_DATA__", "type": "application/json"})
        
        # Check if the script tag exists
        if script_tag:
            # Get the content of the script tag (the JSON data)
            json_data = json.loads(script_tag.string)
            
            # Extract specific part of the data
            if "props" in json_data and "pageProps" in json_data["props"]:
                answers = json_data["props"]["pageProps"].get("answers", None)
                return answers
            else:
                print("Required keys not found in JSON data.")
                return None
        else:
            print("Script tag with id '__NEXT_DATA__' not found.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching the page:", e)
        return None
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        return None

# Example usage
url = "https://connections.swellgarfo.com/nyt/"

with open("data.json", 'w') as json_file:

    json_file.write("[")
    for xx in range(517):

        x = xx+1
        print(x)
        data = scrape_next_data(url+str(x))
        if data:
            key_mapping = {"description":"category"}
            color_mapping = {"#69e352":"green","#fbd400":"yellow","#5492ff":"blue","#df7bea":"purple"}
            for x in range(len(data)):
                data[x] = {key_mapping.get(k, k): v for k, v in data[x].items()}
                data[x]["color"] = color_mapping[data[x]["color"]]
                data[x].pop("emoji")
            x = xx+1
            json.dump(data, json_file, indent=4) # Pretty-print the JSON data
            if(x<517) :
                json_file.write(", \n")
            
    json_file.write("]")
        
