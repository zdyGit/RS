import FileTool

userInfoPath = "\\MoviesDataSet\\u.user"



def GetUserData():

	userLines = FileTool.GetAllDataInline(userInfoPath)
	userList = {}
	for line in userLines:
		userInfoArr = line.strip('\n').split('|')
		user = {}
		user["userID"] = userInfoArr[0]
		user["userAge"] = userInfoArr[1]
		user["userSex"] = userInfoArr[2]
		user["userProfession"] = userInfoArr[3]
		if user["userID"] not in userList.keys():
			userList[user["userID"]] = user
	return userList

def LoadUserInfo():
	print("Load User Data ……")
	ul = GetUserData()
	print("Load User Data Finished !")
	return ul

LoadUserInfo()
