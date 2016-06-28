import FileTool
import AlgorithmSet

userInfoPath = "\\MoviesDataSet\\u.user"
moviesInfoPath = "\\MoviesDataSet\\u.item"
scoreInfoPath = "\\MoviesDataSet\\u.data"

#获取同事信息
def GetUserData():
	userLines = FileTool.GetAllDataInline(userInfoPath)
	userList = {}
	for line in userLines:
		userInfoArr = line.strip('\n').split('|')
		user = {}
		user["userID"] = int(userInfoArr[0])
		user["userAge"] = int(userInfoArr[1])
		user["userSex"] = userInfoArr[2]
		user["userProfession"] = userInfoArr[3]
		if user["userID"] not in userList.keys():
			userList[user["userID"]] = user
	return userList

#获取影片信息
def GetMovieData():
	movieLines = FileTool.GetAllDataInline(moviesInfoPath)
	movieList = {}
	for line in movieLines:
		movieInfoArr = line.strip('\n').split('|')
		movie = {}
		movie["movieID"] = int(movieInfoArr[0])
		movie["title"] = movieInfoArr[1]
		movie["release date"] = movieInfoArr[2]
		movie["video release date"] = movieInfoArr[2]
		movie["IMDb URL"] = movieInfoArr[4]
		movie["unknown"] = int(movieInfoArr[5])
		movie["Action"] = int(movieInfoArr[6])
		movie["Adventure"] = int(movieInfoArr[7])
		movie["Animation"] = int(movieInfoArr[8])
		movie["Children's"] = int(movieInfoArr[9])
		movie["Comedy"] = int(movieInfoArr[10])
		movie["Crime"] = int(movieInfoArr[11])
		movie["Documentary"] = int(movieInfoArr[12])
		movie["Drama"] = int(movieInfoArr[13])
		movie["Fantasy"] = int(movieInfoArr[14])
		movie["Film-Noir"] = int(movieInfoArr[15])
		movie["Horror"] = int(movieInfoArr[16])
		movie["Musical"] = int(movieInfoArr[17])
		movie["Mystery"] = int(movieInfoArr[18])
		movie["Romance"] = int(movieInfoArr[19])
		movie["Sci-Fi"] = int(movieInfoArr[20])
		movie["Thriller"] = int(movieInfoArr[21])
		movie["War"] = int(movieInfoArr[22])
		movie["Western"] = int(movieInfoArr[23])
		if movie["movieID"] not in movieList.keys():
			movieList[movie["movieID"]] = movie
	return movieList

#获取评分记录
def GetScoreData():
	scoreLines = FileTool.GetAllDataInline(scoreInfoPath)
	scoreList = {}
	for line in scoreLines:
		scoreInfoArr = line.strip('\n').split()
		userID = int(scoreInfoArr[0])
		movieID = int(scoreInfoArr[1])
		score = int(scoreInfoArr[2])
		if userID not in scoreList:
			scoreList.setdefault(userID,{})
			scoreList[userID].setdefault(movieID,score)
		else:
			scoreList[userID].setdefault(movieID,score)
	return scoreList


#计算相似度
def GetSimilarityResult(UL,p,n,similarMethod):
	res = {}
	for other in UL:
		if other == p:
			continue
		else:
			res.setdefault(other,similarMethod(UL,p,other))
	return res


def Main():

	ul = GetScoreData()
	p1 = 149
	p2 = 122
	
	si  = AlgorithmSet.GetSameItem(ul,p1,p2)
	for item in si:
		print("p1-"+str(item)+":"+str(ul[p1][item]))
		print("p2-"+str(item)+":"+str(ul[p2][item]))

	print(AlgorithmSet.PearsonSimilarity(ul,p1,p2))
	print(AlgorithmSet.EuclidSimilarity(ul,p1,p2))
	#print(GetSimilarityResult(ul,121,10,AlgorithmSet.EuclidSimilarity))

Main()