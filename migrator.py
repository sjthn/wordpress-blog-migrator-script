import xml.etree.ElementTree as ET

source = "/Users/srijithn/Downloads/therubberduckdev.wordpress.com-2019-11-15-06_51_55/therubberduckdev.wordpress.2019-11-15.post_type-post.author-129349368.status-publish.001.xml"

destination = "/Users/srijithn/PycharmProjects/wordpress_blogs"

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
    file = open(destination + "/" + post.find("wp:post_name", ns).text + ".md", "w")
    file.write(post.find("content:encoded", ns).text)
    count = count + 1

print(f"{count} posts migrated")
