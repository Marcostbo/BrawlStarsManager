from os import environ

API_KEY_BRAWL_STARS = environ.get("API_KEY_BRAWL")
API_URL_BRAWL_STARTS = "https://api.brawlstars.com/v1"
BRAWLERS_ENDPOINT = f"{API_URL_BRAWL_STARTS}/brawlers"
