import csv
import  json

search = input("Search Shop Name: ")
#
#
def find_number(msg):
    for text in msg:
        if '#' in text:
            return text


with open("ShopsLocation.csv", 'rt') as f:
    data = csv.reader(f)
    at_text = find_number(search)
    rep = at_text.replace("#","")
    for row in data:
        if rep in row[1]:
            print(row[0]+"=>"+row[1])
        #     print(row[0] + "=>" + row[1])
       
    print("No Shop of that Name")
