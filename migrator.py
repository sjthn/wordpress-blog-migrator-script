import xml.etree.ElementTree as ET
from datetime import datetime
from os import mkdir
from os import path

source = input("Please provide the path of the file from which to extract ").strip()
if not path.exists(source):
    print("Couldn't find file at specified path")
    exit()

if not source.lower().endswith(".xml"):
    print("Yo!...The source file should be an xml")
    exit()

destination = input("Please provide the directory path where you wanna store the files ").strip()
if not path.isdir(destination):
    if not path.exists(destination):
        mkdir(destination)
    else:
        print("The given destination is not a directory.")
        exit()

ns = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp": "http://wordpress.org/export/1.2/",
}


def filter_posts(xml_element):
    is_post = False
    if xml_element.find("content:encoded", ns) is not None:
        status = xml_element.find("wp:status", ns)
        if status is not None and status.text == "publish":
            is_post = True

    return is_post


tree = ET.parse(source)
root = tree.getroot()

channel = tree.find("channel")

if channel is None:
    print("Aww... sorry couldn't recognize this format")
    exit()

items = channel.findall("item")

if items is None:
    print("Yo... Looks like you haven't written any blog posts")
    exit()

posts = filter(filter_posts, items)

count = 0
for post in posts:
    post_date_time = post.find("wp:post_date", ns).text
    post_date = datetime.strptime(post_date_time, "%Y-%m-%d %H:%M:%S").date()
    file = open(destination + "/" + post_date.__str__() + "-" + post.find("wp:post_name", ns).text + ".md", "w")
    file.write(post.find("content:encoded", ns).text)
    count = count + 1

print(f"{count} posts migrated")
