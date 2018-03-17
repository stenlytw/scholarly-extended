import scholarly
import os
import csv

def paper(filename):	
	search_query = scholarly.search_pubs_query(filename)
	result = next(search_query).fill()
	return result
	
def main():	
	myData = [['No.', 'Title', 'Author', 'Year', 'Citations', 'Type', 'Journal/Conference']]
	number = 0
	
	for file in os.listdir("."):		
		if file.endswith(".pdf"):
			number += 1
			filename = os.path.splitext(file)[0]
			print(number, filename)
			result = paper(filename)
			bib = result.bib
			citedby = getattr(result, 'citedby', 0)
					
			data = []
			data.append(number)
			data.append(bib.get('title', '-'))
			data.append(bib.get('author', '-'))
			data.append(bib.get('year', '-'))
			data.append(citedby)
			
			if bib['ENTRYTYPE'] == 'article':
				data.append('Journal')
				data.append(bib.get('journal', '-'))
			elif bib['ENTRYTYPE'] == 'inproceedings':
				data.append('Conference')
				data.append(bib.get('booktitle', '-'))
			elif bib['ENTRYTYPE'] == 'book':
				data.append('Book')
				data.append(bib.get('publisher', '-'))
			else:
				data.append(bib['ENTRYTYPE'])
				data.append('-')				
			
			myData.append(data)
		
	myFile = open('papers.csv', 'wb')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(myData)		

if __name__ == '__main__':
	main()
