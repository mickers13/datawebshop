from pymongo import MongoClient
import csv

mongo_client = MongoClient('localhost', 27017)

db = mongo_client.huwebshop

ses_col = db.sessions # 3
prof_col = db.profiles # 2
prod_col = db.products # 1

ses_cur = ses_col.find()
prof_cur = prof_col.find()
prod_cur = prod_col.find()
print( prod_cur[1])
# werkend maar mist nog een paar functies:


def writecsv(name, possible_watdanook):
    with open(name, "a", newline='') as file:
        for i in possible_watdanook:
            value_list_watdanook = []
            value_list_watdanook.append(possible_watdanook.index(i))
            value_list_watdanook.append(i)
            inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            inData.writerow(value_list_watdanook)

csvProducten(prod_cur)