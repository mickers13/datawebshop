from pymongo import MongoClient
import csv

mongo_client = MongoClient('localhost', 27017)

db = mongo_client.huwebshop

ses_col = db.sessions # 3
prof_col = db.profiles # 2
prod_col = db.products # 1

ses_cur = ses_col.find().limit(30000)
prof_cur = prof_col.find()
prod_cur = prod_col.find()

def csvWriter(filename, list):
    with open(filename, "a", newline='') as file:
        inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        inData.writerow(list)

def csvSessies(data, filename):
    key_list = ['_id', 'buid', "segment", 'has_sale', 'order', 'events', 'sources']
    for num, i in enumerate(list(data)):
        value_list = []
        order_list = []
        source_list = []
        event_list = []
        buid_list = []
        for y in key_list:
            try:
                if y == '_id':
                    value_list.append(i[y])
                    order_list.append(i[y])
                    event_list.append(i[y])
                    source_list.append(i[y])
                    buid_list.append(i[y])
                elif y == 'buid':
                    for j in i[y]:
                        buid_list.append(j)
                elif y == 'order':
                    if i[y] is not None:
                        for j in i[y]:
                            for c in i[y][j]:
                                for m in c.values():
                                    order_list.append(m)
                        csvWriter('orders.csv', order_list)
                    else:
                        pass
                elif y == 'events':
                    for j in i[y]:
                        for c in j:
                            if c == 'product' and j[c] is not None:
                                event_list.append(j[c])
                    if len(event_list) > 1:
                        csvWriter('events.csv', event_list)
                elif y == 'sources':
                    for j in i[y]:
                        source_list.append(j['full_url'])
                    csvWriter('sources.csv', source_list)
                else:
                    value_list.append(i[y])
            except:
                pass
        csvWriter(filename, value_list)
        csvWriter('buid.csv', buid_list)

csvSessies(ses_cur, 'sessions.csv')
