#pylint:disable=W0312
import csv
import get_review_type_count as grtc
import sort_by_product_id as sort_by_p
import remove_html as rmhtml
import remove_punctuations as rmpunc
import remove_non_english as eng
import remove_stopwords as rmstop
import stem_words as stem

with open("Reviews.csv", "r",encoding="utf8") as file:
	data = csv.reader(file, delimiter=",")
	data = list(data)
	
	head = data[0]
	# head is an array of column heads
	data = data[1:]
	# data is a nested (2 dimensional) array of review data
	# print(len(data))
		
	sorted_data = sort_by_p.apply(data, head.index("ProductId"))
	# sorted_data is a sorted in ascending order of product id
	
	newData = {}
	for (k,v) in enumerate(head):
		newData[v] = [i[k] for i in sorted_data]
	sorted_data = newData
	# sorted_data now reshaped into a dict where each key is a column head
	
	#print(head)
	#print(sorted_data)
	
	pos_neg_count = grtc.apply(sorted_data["Score"])
	# pos_neg_count is a dict of total 'pos' and 'neg' reviews each
	#lower case
	for (t_i, t) in enumerate( sorted_data["Text"] ):
		new_t = rmhtml.apply(t)
		new_t = rmpunc.apply(new_t)
		new_t = eng.apply(new_t)
		new_t = new_t.split(" ")
		new_t2 = []
		for (w_i, w) in enumerate(new_t[:]):
			if w=="": continue
			if len(w) <= 2: continue
			new_t2.append(w.lower())
			
		new_t = " ".join(new_t2)
		# empty substrings have been removed, and the appropriate words have been converted to lower case
				
		new_t = rmstop.apply(new_t)
		# stop words (common words) have been removed
		new_t = stem.apply(new_t)
		# words have been nowmalized
		
		sorted_data["Text"][t_i] = new_t
		
		
	print(sorted_data)

