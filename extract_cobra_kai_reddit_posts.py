import csv




def create_headers_for_csv():
    cobra_kai_s6_finale_data_headers = [["post_id", "title", "body", "created_utc", "score", 
    "num_comments", "url", "bucket", "post_type", ]]
    with open("cobra_kai_s6_finale_post_data.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(cobra_kai_s6_finale_data_headers)








def extract_data_from_cobra_kai_finale_posts():
    with open('cobra_kai_finale_post_links.txt', 'r') as file:
        cobra_kai_reddit_post_links = file.read().splitlines()
    
    


create_headers_for_csv()