import xml.etree.ElementTree as ET
tree = ET.parse(r"C:\Users\andre\PycharmProjects\feedgram\test.xml")
root = tree.getroot()
for item in root.findall('item'):
    title = item.find('title').text
    description = item.find('description').text
    link = item.find('link').text
    print(title, description, link)
