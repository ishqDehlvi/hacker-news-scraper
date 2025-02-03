import requests
import xml.etree.ElementTree as ET

def fetch_top_stories():
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    return response.json()[:10]  # Get top 10 stories

def fetch_story_details(story_id):
    response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
    return response.json()

def generate_xml(stories):
    root = ET.Element("news")
    for story in stories:
        item = ET.SubElement(root, "item")
        ET.SubElement(item, "title").text = story.get("title", "No Title")
        ET.SubElement(item, "url").text = story.get("url", "#")
        ET.SubElement(item, "score").text = str(story.get("score", 0))
    tree = ET.ElementTree(root)
    tree.write("news.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    top_story_ids = fetch_top_stories()
    stories = [fetch_story_details(story_id) for story_id in top_story_ids]
    generate_xml(stories)