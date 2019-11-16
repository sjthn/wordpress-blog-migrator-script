### Python script to migrate blog posts from Wordpress.com to Jekyll

Python script to extract out blog posts content and store them into a markdown file.
Requires Python 3.7.
As of now extracts contents only from published blog posts.

**Steps:**
- Export the blogposts from wordpress.com as xml using export tool provided by wordpress
- Just download and run this script
- Provide the file path as input to the script
- Provide the destination folder as input to the script
- Check the folder for all the extracted posts as markdown files


As of now this script lacks few features mentioned below as TODOs:

- [x] The file name should follow the given format (Year-Month-Day-title.md) for jekyll to recognise it
- [ ] Add post title as front matter on md files (Extract title from xml)
- [ ] Add post layout as front matter on md files (Get as user input)
- [ ] Add mechanism to extract images exported from wordpress and show them for respective posts
- [ ] Add post's original published date as comment on the front matter
