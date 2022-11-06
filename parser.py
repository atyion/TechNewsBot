from urllib.request import urlopen
import xml.etree.ElementTree as ET
read_input = input("Give me the rss's link: ") #Get in input rss's link
url = urlopen(read_input) #Using urlopen to read link
tree = ET.parse(url) #Using xml.etree.ElementTree to parse che xml file
root = tree.getroot() #Using getroot to get the root of the xml file
print(root.tag)
print(root.attrib)
for item in root.findall('channel/item'):
    title = item.find('title').text
    description = item.find('description').text
    link = item.find('link').text
    print(title, description, link, "\n\n")
