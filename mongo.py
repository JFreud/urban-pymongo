import pymongo, random

connection = pymongo.MongoClient("homer.stuy.edu");
db = connection["test"]
restaurants = db["restaurants"]


def borough(boro):
    boro_cursor = restaurants.find({"borough" : boro})
    L = list()
    for restau in boro_cursor:
        L.append(restau)
    return L


def zip(zipco):
    boro_cursor = restaurants.find({"address.zipcode" : zipco})
    L = list()
    for restau in boro_cursor:
        L.append(restau)
    return L

def zip_grade(zipco, grade):
    boro_cursor = restaurants.find({"address.zipcode" : zipco, "grades.grade" : grade})
    L = list()
    for restau in boro_cursor:
        L.append(restau)
    return L

def zip_score(zipco, score):
    boro_cursor = restaurants.find({"address.zipcode" : zipco, "grades.score" : {"$lt": score}})
    L = list()
    for restau in boro_cursor:
        L.append(restau)
    return L

def random_cuisine_in_your_borough_with_a_score_above_a_specified_threshold(boro, cuisine, score):
    boro_cursor = restaurants.find({"borough" : boro, "cuisine" : cuisine, "grades.score" : {"$gte": score}})
    L = list()
    for restau in boro_cursor:
        L.append(restau)
    return random.choice(L)


if __name__ == "__main__":
    # print borough("Manhattan")
    # print zip("11262")
    # print zip_grade("11209", "A")
    # print zip_score("11209", 4)
    # print random_cuisine_in_your_borough_with_a_score_above_a_specified_threshold("Manhattan", "American", 7)
