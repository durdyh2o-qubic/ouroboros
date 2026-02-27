import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "https://theinnermostloop.substack.com/feed"

# Function to fetch the latest post from the RSS feed

def fetch_latest_post():
    response = requests.get(RSS_FEED_URL)
    if response.status_code == 200:
        feed = ET.fromstring(response.content)
        latest_entry = feed.find('item')
        title = latest_entry.find('title').text
        link = latest_entry.find('link').text
        description = latest_entry.find('description').text
        pub_date = latest_entry.find('pubDate').text
        return title, link, description, pub_date
    else:
        print("Failed to fetch feed")
        return None

if __name__ == '__main__':
    latest_post = fetch_latest_post()
    if latest_post:
        title, link, description, pub_date = latest_post
        print(f"Latest Post:")
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Description: {description}")
        print(f"Published Date: {pub_date}")