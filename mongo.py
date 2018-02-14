import pymongo

connection = pymongo.MongoClient("homer.stuy.edu");
db = connection["test"]
restaurants = db["restaurants"]







def borough(boro):
    boro_cursor = restaurants.find({"borough" : boro})
    L = list()
    for restau in boro_cursor:
        L.append(restau)
    return L


def zip():
    return 0

def zip_grade():
    return 0

def zip_score():
    return 0

def smth_clever():
    return 0


if __name__ == "__main__":
    print borough("Manhattan")
