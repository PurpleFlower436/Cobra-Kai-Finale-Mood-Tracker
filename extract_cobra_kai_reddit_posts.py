import csv
import requests
import time
from datetime import datetime
import random
import urllib3

session = requests.Session()
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
        post_labels = ["general_reaction", "general_reaction", "other", "nostalgia_goodbye", "general_reaction", "nostalgia_goodbye", "general_reaction", "general_reaction", "nostalgia_goodbye", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "nostalgia_goodbye", "general_reaction", "character_analysis", "general_reaction", "general_reaction", "nostalgia_goodbye", "character_analysis", "nostalgia_goodbye", "nostalgia_goodbye", "general_reaction", "scene_discussion", "character_analysis", "scene_discussion", "character_analysis", "scene_discussion", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "character_analysis", "scene_discussion", "general_reaction", "general_reaction", "general_reaction", "scene_discussion", "general_reaction", "general_reaction", "scene_discussion", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "general_reaction", "scene_discussion", "general_reaction", "character_analysis", "general_reaction", "nostalgia_goodbye", "scene_discussion", "character_analysis", "general_reaction", "nostalgia_goodbye", "character_analysis", "general_reaction", "character_analysis", "character_analysis", "character_analysis", "character_analysis", "character_analysis", "general_reaction", "character_analysis", "general_reaction", "scene_discussion", "general_reaction", "nostalgia_goodbye", "character_analysis", "scene_discussion", "character_analysis", "character_analysis"]
    for link, classification_label in zip(cobra_kai_reddit_post_links, post_labels):
        url = link + ".json"

        
        
        response = session.get(url, headers=headers, timeout=10)
        data = response.json()

        post = data[0]["data"]["children"][0]["data"]
        utc_timestamp = post["created_utc"]
        dt = datetime.utcfromtimestamp(utc_timestamp)
        
       
        fieldnames = ["post_id","title","body","created_utc","score", 
        "num_comments","url","bucket","post_type"]

        
      
        
        if dt.year == 2025:
            with open("cobra_kai_s6_finale_post_data.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow({
                "post_id": post.get("id", ""),
                "title": post.get("title", ""),
                "body": post.get("selftext", ""),
                "created_utc": post.get("created_utc", ""),
                "score": post.get("ups", 0),
                "num_comments":post.get("num_comments", 0),
                "url":post.get("url", ""),
                "bucket":"immediate",
                "post_type": classification_label})

        else:
                with open("cobra_kai_s6_finale_post_data.csv", "a", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writerow({
                    "post_id": post.get("id", ""),
                    "title": post.get("title", ""),
                    "body": post.get("selftext", ""),
                    "created_utc": post.get("created_utc", ""),
                    "score": post.get("ups", 0),
                    "num_comments":post.get("num_comments", 0),
                    "url":post.get("url", ""),
                    "bucket":"long_term",
                    "post_type": classification_label})


        time.sleep(random.uniform(12, 18))

    
    


append_cobra_kai_season_6_finale_data_to_csv()