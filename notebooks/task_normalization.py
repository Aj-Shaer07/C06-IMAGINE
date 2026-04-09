def normalize(data):
	M=max(data)
	m=min(data)
	normalized_data=[]
	for x in data:
		normalized_data.append((x - m)/(M - m))
	return normalized_data

#main program
print(normalize([3,5,2,6,7,7,3,2]))
