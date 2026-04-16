import csv
import requests
import time
from datetime import datetime
import random
headers = {"User-Agent": "cobra-kai-sentiment-analysis/1.0"}

def create_headers_for_csv():
    cobra_kai_s6_finale_data_headers = [["post_id", "title", "body", "created_utc", "score", 
    "num_comments", "url", "bucket", "post_type", ]]
    with open("cobra_kai_s6_finale_post_data.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(cobra_kai_s6_finale_data_headers)








def append_cobra_kai_season_6_finale_data_to_csv():
    with open('cobra_kai_s6_finale_post_links.txt', 'r') as file:
        cobra_kai_reddit_post_links = file.read().splitlines()
    
    for link in cobra_kai_reddit_post_links:
        url = link + ".json"

        
        
        response = requests.get(url, headers=headers)
        data = response.json()

        post = data[0]["data"]["children"][0]["data"]
        utc_timestamp = post["created_utc"]
        dt = datetime.utcfromtimestamp(utc_timestamp)
        csv_writer = csv.writer(file)
        if dt.year == 2025:
            csv_writer.writerows(post["id"], post["title"], post["selftext"], post["created_utc"], post["ups"],
            post["num_comments"], post["url"], "immediate")
        else:
            csv_writer.writerows(post["id"], post["title"], post["selftext"], post["created_utc"], post["ups"],
            post["num_comments"], post["url"], "long_term")
            


        time.sleep(random.uniform(12, 18))

    
    


append_cobra_kai_season_6_finale_data_to_csv()