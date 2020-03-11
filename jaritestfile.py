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
            with open(filename, "a", newline='') as file:
                inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                inData.writerow(value_list)

csvProducten(prod_cur, 'producten.csv')

###sessies werkt niet, products wel.

def csvSessies(data, filename):
    key_list = ['buid', "segment", 'has_sale', 'order', 'preferences', 'sources']
    for num, i in enumerate(list(data)):
        value_list = []
        key_list_order = []
        key_list_preferences = []
        key_list_sources = []
        if num == 1:
            for y in key_list:
                try:
                    if y == 'buid':
                        for j in i[y]:
                            value_list.append(i[y][j])
                            key_list_order.append(i[y][j])
                            key_list_preferences.append(i[y][j])
                            key_list_sources.append(i[y][j])
                    elif y == 'order':
                        for j in i[y][0]:
                            for k in j:
                                key_list_order.append(k)
                    elif y == 'preferences':
                        for j in i[y]:
                            key_list_preferences.append(j)
                    elif y == 'sources':
                        for j in i[y]:
                            key_list_preferences.append(j)
                    else:
                        value_list.append(i[y])
                except:
                    value_list.append('NULL')
            with open(filename, "a", newline='') as file:
                inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                inData.writerow(value_list)
            with open('orders.csv', "a", newline='') as a:
                inData = csv.writer(a, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                inData.writerow(key_list_order)
            with open('preferences.csv', "a", newline='') as b:
                inData = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                inData.writerow(key_list_preferences)
            with open('sources.csv', "a", newline='') as c:
                inData = csv.writer(c, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                inData.writerow(key_list_preferences)

csvSessies(ses_cur, 'sessions.csv')
