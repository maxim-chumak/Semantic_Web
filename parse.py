import requests
import lxml.html
from bs4 import BeautifulSoup as BS
import xml.etree.ElementTree as ET
from xml.dom import minidom

r = requests.get('https://www.citrus.ua/smartfony/')
html = BS(r.content, 'html.parser')
k=-1

tree = lxml.html.fromstring(r.text)
content = tree.xpath('//meta[@itemprop="sku"]/@content') 

for el in html.select('.product-card__overview'):
	k+=1
	def main():
		ti = el.select('.product-card__name > a')
		pr = el.select('.prices__price')
		hr = ti[0]['href']

		new = ET.Element('all_data')
		phone = ET.SubElement(new, 'phone')
		phone.set('id', content[k])
		name = ET.SubElement(phone, 'name')
		name.text = ti[0]['title']
		price = ET.SubElement(phone, 'price')
		price.text = pr[0].text
		characteristics = ET.SubElement(phone, 'characteristics')

		r2 = requests.get('https://www.citrus.ua' + hr)
		html2 = BS(r2.content, 'html.parser')
		w=-1
		ch = [1,2,3,4,5,6]
		for el2 in html2.select('.desktop .item__description'):
			w+=1
			ch[w] = el2.get_text()
			
		screen_size = ET.SubElement(characteristics, 'characteristics1')
		screen_size.text = ch[0]
		main_camera = ET.SubElement(characteristics, 'characteristics2')
		main_camera.text = ch[1]
		front_camera = ET.SubElement(characteristics, 'characteristics3')
		front_camera.text = ch[2]
		processor = ET.SubElement(characteristics, 'characteristics4')
		processor.text = ch[3]
		number_of_cores = ET.SubElement(characteristics, 'characteristics5')
		number_of_cores.text = ch[4]
		ram_size = ET.SubElement(characteristics, 'characteristics6')
		ram_size.text = ch[5]
	    
		save_xml('test.xml', new)
	 
	def save_xml(filename, xml_code):
		xml_string = ET.tostring(xml_code).decode()

		xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
		with open(filename, 'a', encoding='utf-8') as xml_file:
			xml_file.write(xml_prettyxml)

	if __name__ == '__main__':
		main()