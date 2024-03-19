import xml.etree.ElementTree as ET

tree = ET.parse('examples\movie.xml')
root = tree.getroot()

# print(root.tag)

# print(root.attrib)

# for child in root:
#     print(child.tag, child.attrib)

"""
In this code, each movie element is iterated through. Thereafter, for each movie,
the elements are looped through and their tags are printed.
"""
for movie in root.iter('movie'):
    for el in movie:
        print(el.tag)

    break # this will end the loop after iterating through one movie

"""
In this code, each movie element is iterated through. Thereafter, for each movie,
the elements are looped through. If the tag matches the search term "description"
then the text of that tag is printed.
"""
for movie in root.iter('movie'):  
    for el in movie:
        if el.tag == 'description':
            print(''.join(el.itertext()))
    

"""
In this code, each movie element is iterated through. 
The attributes of the movie elements are then retrieved as a dictionary. 
The value of the "favorite" attribute is then checked to see if its true or not.
If true, then the fave counter is incremented, else the not_fave counter is incremented.
"""
fave = 0
not_fave = 0
for movie in root.iter('movie'):

    if movie.attrib["favorite"].lower() == "true":
        fave += 1
    
    else:
        not_fave += 1

print('Favourites:', fave)
print('Not Favourites:', not_fave)