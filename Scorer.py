
def score_darts(starting_score, hits):
	total_hit_score = 0

	for sublist in hits:
		#print("sublist"+str(sublist))
		#print("hits"+str(hits))
		for hit in sublist:
			#print("hit"+str(hit))
			#print("sublist"+str(sublist))
			#Ensure the `hit` is a valid [points, is_double] pair
			if isinstance(hit, list) and len(hit) == 2 and isinstance(hit[0], int) and isinstance(hit[1], bool):
				total_hit_score += hit[0]
				double = hit[1]
				if ((starting_score - total_hit_score == 0) and(double)):
					return 1000 #win

	if starting_score - total_hit_score > (50):
		return total_hit_score
	elif starting_score - total_hit_score <= 1:
		return -1
	else:
		return score_sub_51(starting_score - total_hit_score, total_hit_score)

def score_sub_51(finish_score,hitscore):
	
	if finish_score < 21:
		if finish_score % 2 == 0:
			return (180) + finish_score
		elif (finish_score + hitscore) < 21:
			-hitscore
	return hitscore 


##hits = [[[20, False],[100,200]], [[30,True],[100,300]], [[10,True],[200,259]]]
#hits = [[[60, False]]]
#print(score_darts((501-360), hits)) 