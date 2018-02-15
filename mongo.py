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
    boro_cursor = restaurants.find({"address.zipcode" : zipco, "grades[0].grade" : grade})
    L = list()
    for restau in boro_cursor:
        L.append(restau)
    return L

def zip_score(zipco, score):
    boro_cursor = restaurants.find({"address.zipcode" : zipco, "grades[0].score" : {$lt: score}})
    return 0

def random_cuisine_in_your_borough_with_a_score_below_a_specified_threshold(boro, cuisine, score):
    boro_cursor = restaurants.find({"borough" : boro, "cuisine" : cuisine, "grades[0].score" : {$lt: score}})
    L = list()
    for restau in boro_cursor:
        L.append(restau)
    return random.choice(L)


if __name__ == "__main__":
    print borough("Manhattan")
    print zip("11262")
    print zip_grade("11262", "A")
    print zip_score("11262", "7")
    print random_cuisine_in_your_borough_with_a_score_below_a_specified_threshold("Manhattan", "American", "7")
