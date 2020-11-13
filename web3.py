import xml.etree.ElementTree as ET

data ='''<stuff>
                <citizen>
                    <person>
                        <name>Jay</name>
                        <phone type="int">+91 1234567892</phone>
                        <email hide="yes" />
                    </person>
                    <person>
                        <name>Ketul</name>
                        <phone type="int">+91 4569823149</phone>
                        <email hide="yes" />
                    </person>
               </citizen>
        </stuff>'''

tree = ET.fromstring(data)
listpr = tree.findall('citizen/person')
print("Total Citizen :",len(listpr))
for pr in listpr:
    print("Name:",pr.find('name').text)
    print("Phone:",pr.find('phone').text)
