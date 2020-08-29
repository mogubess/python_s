from termcolor import colored

from collections import defaultdict
import csv

def askQuesion(hname, fdict):
    favorite_restaurant = input("{inputname} さんどこのレストランが好きですか？\n".format(inputname=hname))
    fdict[favorite_restaurant.title()] += 1


humanName = input(colored('こんにちは、あなたのお名前は？\n', 'green'))

# 好みを登録しているデータがあるかを確認する
restaurantDict = defaultdict(int)
try:
    with open('section9.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            restaurantDict[row['NAME']] = int(row['COUNT'])
    
except FileNotFoundError as exc:
    pass
finally:
    pass

# if 好みのデータが一個でも登録されているか？
if len(restaurantDict) > 0:
    #一番多い登録数でソートする
    sortRestaurantDict = sorted(restaurantDict.items(), key=lambda x:x[1], reverse=True)
    #mostPopulraRestaurant = next(iter(sortRestaurantDict))
    for restaurantName in sortRestaurantDict:
        print("私のおすすめは{restaurant}です".format(restaurant=restaurantName[0]))
        choice = input("このレストランは好きですか？ [Yes/No]")
        if choice in ['Yes','YES','y', 'ye', 'yes']:
            #好きな場合はカウントを加算する
            restaurantDict[restaurantName[0].title()] += 1
            break
    else:
        #改めて好きなレストランを聞く
        #favorite_restaurant = input("{inputname} さんどこのレストランが好きですか？\n".format(inputname=humanName))
        #restaurantDict[favorite_restaurant.title()] += 1
        askQuesion(humanName,restaurantDict)
else:
    #データが１個も登録されいていない
    askQuesion(humanName,restaurantDict)
    # favorite_restaurant = input("{inputname} さんどこのレストランが好きですか？\n".format(inputname=humanName))
    # restaurantDict[favorite_restaurant.title()] += 1

print(colored("""
Roboco: Junさん、ありがとうございました
良い一日を！
""",'green'))

with open('section9.csv', 'w') as csv_file:
    fieldnames = ['NAME', 'COUNT']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for key,val in restaurantDict.items():
        print(key, val)
        writer.writerow({'NAME': key, 'COUNT':val})