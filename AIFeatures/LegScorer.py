def score_darts_leg(starting_score, hits):
	total_hit_score = 0
	for hit in hits:
		points, is_double = hit
		total_hit_score += points
	if starting_score - total_hit_score > 180:
		return total_hit_score
	elif ((starting_score - total_hit_score) == 0 )and (hits[-1][1] == True) :
		return float('inf') #Win
	elif starting_score - total_hit_score <= 1:
		return -1
	else: 
		return score_sub_181(starting_score - total_hit_score, total_hit_score)

def score_sub_181(finish_score,hitscore):
	if finish_score < 21:
		if finish_score % 2 == 0:
			return 180 + finish_score
		elif (finish_score + hitscore) < 21:
			-hitscore
	return hitscore 


hits = [[20, False], [30,True], [10,False]]
print(score_darts_leg(60, hits)) 