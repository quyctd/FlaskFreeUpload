import pymongo

#mongodb://htrieu:prototype101@ds263832.mlab.com:63832/final_project_c4e20


client = pymongo.MongoClient("mongodb://htrieu:prototype101@ds263832.mlab.com:63832/final_project_c4e20")

db = client.final_project_c4e20

col = db.recipe.find({})

for doc in col:
    ing = doc['ingredients']
    list_search = ['beef', 'oil']
    count = 0
    for item in list_search:
        l = [x for x in ing if item in x]
        if len(l) != 0:
            count += 1 
    if count == len(list_search):
        print(ing)
