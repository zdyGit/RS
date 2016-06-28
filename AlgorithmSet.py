import math

#得到两者共同评分项
def GetSameItem(UL,p1,p2):
	si = {}
	for item in UL[p1]:
		if item in UL[p2]:
			si[item] = 1
	return si

#欧几里得相似度算法
def EuclidSimilarity(UL,p1,p2):
	si = GetSameItem(UL,p1,p2)
	if len(si) == 0:
		return 0
	sum_of_squares = sum([pow(UL[p1][item] - UL[p2][item] , 2) for item in si])
	return 1/(1+math.sqrt(sum_of_squares))

#皮尔逊相似度算法
def PearsonSimilarity(UL,p1,p2):
	si = GetSameItem(UL,p1,p2)
	n = len(si)
	if n == 0:
		return 0

	sum1 = sum([UL[p1][item] for item in si])
	sum2 = sum([UL[p2][item] for item in si])

	sqSum1 = sum([pow(UL[p1][item],2) for item in si])
	sqSum2 = sum([pow(UL[p2][item],2) for item in si])

	pSum = sum([UL[p1][item]*UL[p2][item] for item in si])

	num = pSum - (sum1*sum2/n)
	den = math.sqrt(sqSum1-pow(sum1,2)/n)*math.sqrt(sqSum2-pow(sum2,2)/n)

	if den ==0:
		return 0

	r = num/den
	return r

#矩阵转换
def Transfer(UL):
	res = {}
	for user in UL:
		for movie in UL[user]:
			res.setdefault(movie,{})
			res[movie][user] = UL[user][movie]
	return res