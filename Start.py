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

#统计与某人最相似的n个人
def GetSimilarityResult(UL,p,n,similarMethod):
	
	res = [(other,similarMethod(UL,p,other)) for other in UL if other != p]
	res.sort(key = lambda x:x[1],reverse = True)
	return res[0:n]

#根据指定相似度算法给某人推荐n部电影
def GetRecommendMovies(UL,p,n,similarMethod):

	totalScore = {}
	simSums = {}
	for other in UL:
	 	if other == p :
	 		continue
	 	else:
	 		sim = similarMethod(UL,p,other)

	 		if sim >0:
	 			for item in UL[other]:
	 				if item not in UL[p] or UL[p][item] == 0:
	 					totalScore.setdefault(item,0)
	 					totalScore[item] += UL[other][item]*sim
	 					simSums.setdefault(item,0)
	 					simSums[item] += sim

	rankings = [ (total/simSums[item],item) for item,total in totalScore.items() ]
	rankings.sort(reverse=True)
	return rankings[0:n]

def Main():

	mi = GetMovieData()
	ul = GetScoreData()

	#print(AlgorithmSet.PearsonSimilarity(ul,12,13))
	#print(AlgorithmSet.EuclidSimilarity(ul,12,13))
	#
	#print(GetSimilarityResult(ul,12,5,AlgorithmSet.PearsonSimilarity))

	#s1 = GetRecommendMovies(ul,87,30,AlgorithmSet.PearsonSimilarity)
	#for item in s1:
	#	print(str(item[0])+":"+mi[item[1]]["title"])		
	ml = AlgorithmSet.Transfer(ul)
	print(GetRecommendMovies(ml,1,10,AlgorithmSet.PearsonSimilarity))

Main()