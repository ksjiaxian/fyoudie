#########################################################################################################################
# Vectorize a restaurant given its Yelp data
########################################################################################################################


import json

business_file_path = "yelp_dataset/yelp_academic_dataset_business.json"
review_file_path = "yelp_dataset/yelp_academic_dataset_review.json"

business_info_dict = {}
with open(business_file_path, 'r') as business_data:
	for b in business_data:
		b_dict = json.loads(b)

		bid = b_dict['business_id']
		category = b_dict["categories"]
		if (category is None) :
			continue
		else:
			if ("Restaurants" in category):
				business_info_dict[bid] = b_dict

print(len(business_info_dict))

restaurant_ids = business_info_dict.keys()
# print(restaurant_ids)
review_info_dict = {}
with open(review_file_path, 'r') as review_data:
	for r in review_data:
		r_dict = json.loads(r)

		bid = r_dict['business_id']
		# print(bid)
		if (bid in restaurant_ids): # this is a restaurant
			if (bid in review_info_dict):
				review_info_dict[bid].append(r_dict)
			else:
				review_info_dict[bid] = [r_dict]

print(len(review_info_dict))

