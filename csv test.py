import csv
#bron hoe csv te gebruiken: https://docs.python.org/2/library/csv.html
def writeCsvList(data, filename, type):
    '''Pak de list, en plak deze direct in de row. hierdoor krijg je een row met een list per cell in de kloppende row en voeg in row van goede type
    Om deze functie te gebruiken importeer deze file en gebruik de functie.
    '''
    with open(filename, "a") as opslag:
        inData = csv.writer(opslag, delimiter= ',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)



        if type == 1:
            inData.writerow([data,'',''])
        elif type == 2:
            inData.writerow(['',data,''])
        elif type == 3:
            inData.writerow(['', '' , data])


# voorbeeld van gebruiken:
test = ["data1","data2","data3 of meer"]
writeCsvList(test,"test.csv",2)
writeCsvList(test, "test.csv", 3)