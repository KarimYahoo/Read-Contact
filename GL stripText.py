import docx

def setText(fileText):
	fileText2 = []
	fileText3 = []
	fileText4 = ''
	for i in fileText:
		fileText2.append(i.strip('\n'))

	for i in fileText2:
		fileText3.append(i.strip('\t'))	
	
	return ' '.join(fileText3)
