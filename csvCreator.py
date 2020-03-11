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
                    if i[y] in possible_subcategories:
                        value_list.append(possible_subcategories.index(i[y]))
                    else:
                        possible_subcategories.append(i[y])
                        value_list.append(possible_subcategories.index(i[y]))
                elif y == 'subsubcategory':
                    if i[y] in possible_subsubcategories:
                        value_list.append(possible_subsubcategories.index(i[y]))
                    else:
                        possible_subsubcategories.append(i[y])
                        value_list.append(possible_subsubcategories.index(i[y]))
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
            with open("producten.csv", "a", newline='') as file:
                inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                inData.writerow(value_list)
    writecsv("doelgroep.csv", possible_doelgroepen)
    writecsv("gender.csv", possible_gender)
    writecsv("brands.csv", possible_brands)
    writecsv("categories.csv", possible_categories)

def writecsv(name, possible_watdanook):
    with open(name, "a", newline='') as file:
        for i in possible_watdanook:
            value_list_watdanook = []
            value_list_watdanook.append(possible_watdanook.index(i))
            value_list_watdanook.append(i)
            inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            inData.writerow(value_list_watdanook)

csvProducten(prod_cur)