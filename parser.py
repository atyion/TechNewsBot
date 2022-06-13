import xml.etree.ElementTree as ET
tree = ET.parse(r"PATH")
root = tree.getroot()
print(root.tag)
print(root.attrib)
for item in root.findall('channel/item'):
    title = item.find('title').text
    description = item.find('description').text
    link = item.find('link').text
    print(title, description, link, "\n\n")
