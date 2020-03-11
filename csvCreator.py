from pymongo import MongoClient
import csv

mongo_client = MongoClient('localhost', 27017)

db = mongo_client.huwebshop

ses_col = db.sessions # 3
prof_col = db.profiles # 2
prod_col = db.products # 1

ses_cur = ses_col.find().limit(10000)
prof_cur = prof_col.find().limit(10000)
prod_cur = prod_col.find().limit(10000)


def csvWriter(filename, list):
    try:
        with open(filename, "a", newline='') as file:
            inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            inData.writerow(list)
    except:
        print(Exception)
        pass


def writecsv(name, possible_watdanook):
    with open(name, "a", newline='') as file:
        for i in possible_watdanook:
            value_list_watdanook = []
            value_list_watdanook.append(possible_watdanook.index(i))
            value_list_watdanook.append(i)
            inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            inData.writerow(value_list_watdanook)


def csvProfiles(data, filename):
    key_list = ['_id', 'recommendations']
    key_list_recommendations = ['segment']
    for profile in list(data):
        value_list = []
        for key in key_list:
            try:
                if key == 'recommendations':
                    for recommendations_key in profile[key]:
                        if recommendations_key in key_list_recommendations:
                            value_list.append(profile[key][recommendations_key])
                else:
                    value_list.append(profile[key])
            except:
                value_list.append('NULL')
        csvWriter(filename, value_list)


def csvProducten(data):
    key_list = ['_id', 'name','gender','category','subcategory','subsubcategory', 'brand', 'price', 'herhaalaankopen', 'color', 'description', 'properties', 'size']
    key_list_price = ['selling_price', 'discount']
    key_list_properties = ['eenheid', 'inhoud', 'leeftijd', 'serie', 'soort', 'sterkte', 'tax', 'weekdeal', 'doelgroep']
    possible_gender = []
    possible_brands = []
    possible_doelgroepen = []
    possible_categories = []
    possible_subcategories = []
    possible_subsubcategories = []
    for num, i in enumerate(list(data)):
        value_list = []
        for y in key_list:
            try:
                if y == 'brand':
                    print(i[y])
                    if i[y] in possible_brands:
                        value_list.append(possible_brands.index(i[y]))
                        print(value_list)
                    else:
                        possible_brands.append(i[y])
                        value_list.append(possible_brands.index(i[y]))
                elif y == 'gender':
                    if i[y] in possible_gender:
                        value_list.append(possible_gender.index(i[y]))
                        print(value_list)
                    else:
                        possible_gender.append(i[y])
                        value_list.append(possible_gender.index(i[y]))
                elif y == 'category':
                    if i[y] in possible_categories:
                        value_list.append(possible_categories.index(i[y]))
                    else:
                        possible_categories.append(i[y])
                        value_list.append(possible_categories.index(i[y]))
                elif y == 'subcategory':
                    try:
                        if i[y] in possible_subcategories:
                            value_list.append(possible_categories.index(i[y]))
                        else:
                            possible_subcategories.append(i[y])
                            value_list.append(possible_categories.index(i[y]))
                    except:
                        pass
                elif y == 'subsubcategory':
                    try:
                        if i[y] in possible_subsubcategories:
                            value_list.append(possible_categories.index(i[y]))
                        else:
                            possible_subsubcategories.append(i[y])
                            value_list.append(possible_categories.index(i[y]))
                    except:
                        pass
                elif y == 'price':
                    for j in i[y]:
                        if j in key_list_price:
                            value_list.append(i[y][j])
                elif y == 'properties':
                    for j in i[y]:
                        if j in key_list_properties:
                            if j == "doelgroep":
                                possible_doelgroepen.append(i[y][j])
                                value_list.append(possible_doelgroepen.index(i[y][j]))
                            else:
                                value_list.append(i[y][j])
                else:
                    value_list.append(i[y])
            except:
                print(Exception)
                pass
        csvWriter('products.csv', value_list)
    writecsv("doelgroep.csv", possible_doelgroepen)
    writecsv("gender.csv", possible_gender)
    writecsv("brands.csv", possible_brands)
    writecsv("categories.csv", possible_categories)


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
csvProfiles(prof_cur, 'profiles.csv')
csvProducten(prod_cur)
