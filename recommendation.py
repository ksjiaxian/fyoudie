import csv
# a set of restaurants
restaurant_features = {}
with open('data/restaurant_features.csv') as rest_vec_file:
    rest_vec_reader = csv.reader(rect_vec_file, delimiter=',')
    for row in rest_vec_reader:
        restaurant_features[row[0]] = row[1:]

# a profile of a user
user_id = 'randomuid'
with open('data/user_features.csv') as user_vec_file:
    user_vec_reader = csv.reader(user_vec_file, delimiter=',')
    for row in user_vec_reader:
        if row[0] == user_id:
            user_feature = row[1:]

# a user defined by their history
user_history_list = []
user_rest_set = set()
with open('data/user_retaurant.csv') as user_history_file:
    user_history_reader = csv.reader(user_history_file, delimiter=',')
    for row in user_history_reader:
        if row[0] == user_id:
            user_history.append(row[1], row[2], row[3])
            user_rest_set.add(row[1])

sorted_user_history = sorted(user_history, key=lambda t: t[3])

# filter
res = []
for restaurant_id in restaurant_features.keys():
    # if it exists in the set, early continue
    if restaurant_id in user_rest_set:
        continue
    flag = sum([u & r for u,r in zip(user_feature, restaurant_features[restaurant_id])])
    res.append((restaurant_id, flag))
sorted_res = sorted(res, key=lambda t: t[1])