import requests
import os
from tqdm import tqdm

BASE_URL = "https://dumps.wikimedia.org"
WIKI_PROJECT = "enwiki"
DUMP_TYPE = "latest"
OUTPUT_DIR = "./wikipedia/wikipedia_sql_dumps"

SQL_FILES = [
    "site.sql.gz",
    "category.sql.gz",
    "page.sql.gz",
    "revision.sql.gz",
    "text.sql.gz",
    "pagelinks.sql.gz"
]

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_file(url, output_path):
    """Download a file with a progress bar."""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(output_path, "wb") as file, tqdm(
        desc=f"Downloading {os.path.basename(output_path)}",
        total=total_size,
        unit="B",
        unit_scale=True
    ) as bar:
        for data in response.iter_content(1024):
            bar.update(len(data))
            file.write(data)

def main():
    for sql_file in SQL_FILES:
        file_url = f"{BASE_URL}/{WIKI_PROJECT}/{DUMP_TYPE}/{WIKI_PROJECT}-{DUMP_TYPE}-{sql_file}"
        output_path = os.path.join(OUTPUT_DIR, sql_file)

        if not os.path.exists(output_path):
            print(f"Downloading {sql_file}...")
            download_file(file_url, output_path)
            print(f"Downloaded: {output_path}")
        else:
            print(f"File already exists: {output_path}")

if __name__ == "__main__":
    main()