import os



def GetAllDataInline(filePath):
	filePath = os.getcwd() + filePath
	if os.path.exists(filePath):
		file_object = open(filePath)
		try:
			lines = file_object.readlines();
		finally:
			file_object.close()
		return lines
	else:
		print(False)
	
	