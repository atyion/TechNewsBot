from urllib.request import urlopen
import xml.etree.ElementTree as ET

def parser():
    #read_input = input("Give me the rss's link: ") #Get in input rss's link
    url = urlopen('https://feeds.a.dj.com/rss/RSSWSJD.xml') #Using urlopen to read link
    tree = ET.parse(url) #Using xml.etree.ElementTree to parse che xml file
    root = tree.getroot() #Using getroot to get the root of the xml file
    #print(root.tag)
    #print(root.attrib)
    for item in root.findall('channel/item'):
        title = item.find('title').text
        description = item.find('description').text
        link = item.find('link').text
        date = item.find('pubDate').text
        date = date[0:len(date)-6]
        return [title, description, link, date]

'''
parser()[0] ==> title

parser()[1] ==> description

parser()[2] ==> link

parser()[3] ==> date

THE LAST ARTICLE!

'''
