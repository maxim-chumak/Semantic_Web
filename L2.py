import lxml.html
from lxml import etree
import xml.etree.ElementTree as ET
from xml.dom import minidom


tree = ET.parse('test.xml')
root = tree.getroot()

def main():
	k=0
	for phone in root.findall('phone'):
		k+=1
			
		price = phone.find('price')
		item_price = price.text.split()
		item_price = ''.join(item_price)
		item_price = float(item_price[0:-3])
		phone.set('id', str(k))
		price.text = str(item_price)

		country = ET.SubElement(phone, 'country')
		country1 = ET.SubElement(country, 'country1')
		country1.text = 'China'
		country2 = ET.SubElement(country, 'country2')
		country2.text = 'France'
		country3 = ET.SubElement(country, 'country3')
		country3.text = 'Germany'

		if item_price < 5000.00:
			root.remove(phone)

	save_xml('L2.xml', root)
	 
def save_xml(filename, xml_code):
	xml_string = ET.tostring(xml_code).decode()
	xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
	with open(filename, 'w', encoding='utf-8') as xml_file:
		xml_file.write(xml_prettyxml)

main()

xslt_doc = etree.parse("L2.xslt")
xslt_transformer = etree.XSLT(xslt_doc)
 
source_doc = etree.parse("L2.xml")
output_doc = xslt_transformer(source_doc)

output_doc.write("output-toc.html", pretty_print=True)