import scholarly
import os
import csv
import pprint

def paper(filename):	
	search_query = scholarly.search_pubs_query(filename)
	result = next(search_query).fill()
	return result
	
def main():	
	myData = [['No.', 'Title', 'Author', 'Year', 'Citations', 'Type', 'Journal/Conference']]
	number = 0
	
	for file in os.listdir("."):		
		if file.endswith(".pdf"):
			filename = os.path.splitext(file)[0]
			result = paper(filename)
			bib = result.bib
			citedby = result.citedby
			#~ pprint.pprint(bib)	
					
			data = []
			number += 1
			data.append(number)
			data.append(bib['title'])
			data.append(bib['author'])
			data.append(bib['year'])
			data.append(citedby)
			
			if bib['ENTRYTYPE'] == 'article':
				data.append('Journal')
				data.append(bib['journal'])
			else:
				data.append('Conference')
				data.append(bib['booktitle'])
			
			myData.append(data)
	
	print myData		
	myFile = open('papers.csv', 'wb')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(myData)		

if __name__ == '__main__':
	main()
