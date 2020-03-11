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
def csvProducten(data, filename):
    key_list = ['_id', 'name','gender', 'brand', 'price', 'herhaalaankopen', 'color', 'description', 'properties', 'size']
    key_list_price = ['selling_price', 'discount']
    key_list_properties = ['eenheid', 'inhoud', 'leeftijd', 'serie', 'soort', 'sterkte', 'tax', 'weekdeal']
    possible_gender = []
    possible_brands = []
    for num, i in enumerate(list(data)):
        value_list = []
        if num == 1 or num == 2:
            for y in key_list:
                if y == 'brand':
                    print(i[y])
                    if i[y] in possible_brands:
                        value_list.append(possible_brands.index(i[y]))
                        print(value_list)
                    else:
                        possible_brands.append(i[y])
                        value_list.append(possible_brands.index(i[y]))
                elif y == 'gender':
                    print(i[y])
                    if i[y] in possible_gender:
                        value_list.append(possible_gender.index(i[y]))
                        print(value_list)
                    else:
                        possible_gender.append(i[y])
                        value_list.append(possible_gender.index(i[y]))
                elif y == 'price':
                    for j in i[y]:
                        if j in key_list_price:
                            value_list.append(i[y][j])
                elif y == 'properties':
                    for j in i[y]:
                        if j in key_list_properties:
                            value_list.append(i[y][j])
                else:
                    value_list.append(i[y])
            with open("producten.csv", "a", newline='') as file:
                inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                inData.writerow(value_list)
    writecsv("gender.csv", possible_gender)
    writecsv("brands.csv", possible_brands)

def writecsv(name, possible_watdanook):
    with open(name, "a", newline='') as file:
        for i in possible_watdanook:
            value_list_watdanook = []
            value_list_watdanook.append(possible_watdanook.index(i))
            value_list_watdanook.append(i)
            inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            inData.writerow(value_list_watdanook)





csvProducten(prod_cur, 'producten.csv')

# with open("gender.csv", "a", newline='') as file:
    #     for i in possible_gender:
    #         value_list_gender = []
    #         value_list_gender.append(possible_gender.index(i))
    #         value_list_gender.append(i)
    #         inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #         inData.writerow(value_list_gender)
# ###sessies werkt niet, products wel.
#
# def csvSessies(data, filename):
#     key_list = ['buid', "segment", 'has_sale', 'order', 'preferences', 'sources']
#     for num, i in enumerate(list(data)):
#         value_list = []
#         key_list_order = []
#         key_list_preferences = []
#         key_list_sources = []
#         if num == 1:
#             for y in key_list:
#                 try:
#                     if y == 'buid':
#                         for j in i[y]:
#                             value_list.append(i[y][j])
#                             key_list_order.append(i[y][j])
#                             key_list_preferences.append(i[y][j])
#                             key_list_sources.append(i[y][j])
#                     elif y == 'order':
#                         for j in i[y][0]:
#                             for k in j:
#                                 key_list_order.append(k)
#                     elif y == 'preferences':
#                         for j in i[y]:
#                             key_list_preferences.append(j)
#                     elif y == 'sources':
#                         for j in i[y]:
#                             key_list_preferences.append(j)
#                     else:
#                         value_list.append(i[y])
#                 except:
#                     value_list.append('NULL')
#             with open(filename, "a", newline='') as file:
#                 inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                 inData.writerow(value_list)
#             with open('orders.csv', "a", newline='') as a:
#                 inData = csv.writer(a, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                 inData.writerow(key_list_order)
#             with open('preferences.csv', "a", newline='') as b:
#                 inData = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                 inData.writerow(key_list_preferences)
#             with open('sources.csv', "a", newline='') as c:
#                 inData = csv.writer(c, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                 inData.writerow(key_list_preferences)
#
# csvSessies(ses_cur, 'sessions.csv')
