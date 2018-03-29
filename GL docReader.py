import docx
import stripText
import csv
import contractHeaders

# Read in the document
doc = docx.Document('general liability policy Single Column2.docx')

# Define Arrays/Variables
fullText = []
fullText2 = ''
Sections = []
Sec = []

# Read in the word document
for para in doc.paragraphs:
	fullText.append(para.text)


#This strips some of the non-sense		
fullText2 = stripText.setText(list(fullText))
fullText2 = fullText2.replace(',','')

#This are the variables that need to be changed by contract
Sec = contractHeaders.setHeaders('GL')


#This finds the location of each of titles
for i in range(0, len(Sec)):
	Sections.append(fullText2.find(Sec[i]))

print(Sections)
#This is the CSV portion
outputFile = open('gl_output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
out = []

for i in range(0,len(Sections)):
	if i <len(Sections) -1:
		a = Sections[i] + len(Sec[i])
		b = Sections[i+1]
		out.append(fullText2[a:b])
	else:
		a = Sections[i] + len(Sec[i])
		out.append(fullText2[a:])
		

outputWriter.writerow(Sec)
outputWriter.writerow(out)


