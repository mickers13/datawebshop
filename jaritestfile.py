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


def csvProducten(data, filename):
    key_list = ['_id', 'name', 'price', 'herhaalaankopen', 'color', 'description', 'properties', 'size']
    key_list_price = ['selling_price', 'discount']
    key_list_properties = ['eenheid', 'inhoud', 'leeftijd', 'serie', 'soort', 'sterkte', 'tax', 'weekdeal']
    for num, i in enumerate(list(data)):
        value_list = []
        if num == 1 or num == 2:
            for y in key_list:
                try:
                    if y == 'price':
                        for j in i[y]:
                            if j in key_list_price:
                                value_list.append(i[y][j])
                    elif y == 'properties':
                        for j in i[y]:
                            if j in key_list_properties:
                                value_list.append(i[y][j])
                    else:
                        value_list.append(i[y])
                        print(i[y])
                except:
                    value_list.append('NULL')
            csvWriter(filename, value_list)

#csvProducten(prod_cur, 'producten.csv')

###sessies werkt niet, products wel.

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
