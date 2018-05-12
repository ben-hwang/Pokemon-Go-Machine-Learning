from bs4 import BeautifulSoup

import os

import datetime

import re

import pandas as pd
#====================================================================================================
#this part gets all of the keys for the dictionary

folders = []

for folder in os.listdir('./pokemon go data'):
	if folder != '.DS_Store':
		folders.append(folder)

folders.sort()

dates_set = {datetime.datetime(2016, 7, 21, 0, 0, 0)}

for folder in folders:
	year = folder[0:4]
	month = folder[5:7]
	day = folder[8:10]

	for file in os.listdir('./pokemon go data' + '/' + str(folder)):
		hour = file[0:2]
		minute = file[3:5]
		new_date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), 0)
		dates_set.add(new_date)

#these holds all the keys for dictionary
dates = sorted(dates_set)
#print(len(dates)) == 1584

#====================================================================================================
#this part gets all of the values for the dictionary and put everything in dictionary
final_dict = {}
dict_holder = []

files_21 = []
files_22 = []
files_23 = []
files_24 = []
files_25 = []
files_26 = []
files_27 = []
files_28 = []
files_29 = []
files_30 = []
files_31 = []

#helper function that imitates a switch statement 
def switch(x):
    return {
        '21': files_21,
        '22': files_22,
        '23': files_23,
        '24': files_24,
        '25': files_25,
        '26': files_26,
        '27': files_27,
        '28': files_28,
        '29': files_29,
        '30': files_30,
        '31': files_31,
    }[x]

for x in range(21, 32):
	for file in os.listdir('./pokemon go data' + '/2016-07-' + str(x)):
		switch(str(x)).append(file)

files_21.sort()
files_22.sort()
files_23.sort()
files_24.sort()
files_25.sort()
files_26.sort()
files_27.sort()
files_28.sort()
files_29.sort()
files_30.sort()
files_31.sort()

#print(len(files_30))  == 288

#should be range(21,32)
#should be range(0,288)

for y in range(21,32):
    print('ITERATION' + str(y))
    for x in range(0,288):
        if x % 2 == 0:
            #android
            if y == 21:
                r = open('pokemon go data/2016-07-21/' + str(files_21[x]), 'r')
            elif y == 22:
                r = open('pokemon go data/2016-07-22/' + str(files_22[x]), 'r')
            elif y == 23:
                r = open('pokemon go data/2016-07-23/' + str(files_23[x]), 'r')
            elif y == 24:
                r = open('pokemon go data/2016-07-24/' + str(files_24[x]), 'r')
            elif y == 25:
                r = open('pokemon go data/2016-07-25/' + str(files_25[x]), 'r')
            elif y == 26:
                r = open('pokemon go data/2016-07-26/' + str(files_26[x]), 'r')
            elif y == 27:
                r = open('pokemon go data/2016-07-27/' + str(files_27[x]), 'r')
            elif y == 28:
                r = open('pokemon go data/2016-07-28/' + str(files_28[x]), 'r')
            elif y == 29:
                r = open('pokemon go data/2016-07-29/' + str(files_29[x]), 'r')
            elif y == 30:
                r = open('pokemon go data/2016-07-30/' + str(files_30[x]), 'r')
            elif y == 31:
                r = open('pokemon go data/2016-07-31/' + str(files_31[x]), 'r')
            
            soup = BeautifulSoup(r, 'lxml')
        
            #r = urlopen('file://' + os.getcwd() + '/pokemon go data/2016-07-21/' + str(files_21[x])).read()
            #soup = BeautifulSoup(r, 'html.parser')
        
            res = soup.findAll("div", {"class":"rating-box"})
            res_holder = []
        
            #================================================================================
            #METHOD 1:
            #================================================================================
            for element in res:
                for element1 in element:
                    for element2 in element1:
                        for element3 in element2:
                            res_holder.append(element3)
            
            try:
                android_avg_rating = float(res_holder[4])
                android_total_ratings = int(res_holder[13].string.replace(",",""))
                android_rating_5 = int(res_holder[23].string.replace(",",""))
                android_rating_4 = int(res_holder[30].string.replace(",",""))
                android_rating_3 = int(res_holder[37].string.replace(",",""))
                android_rating_2 = int(res_holder[44].string.replace(",",""))
                android_rating_1 = int(res_holder[51].string.replace(",",""))
            except:
                android_avg_rating = 696969
                android_total_ratings = 696969
                android_rating_5 = 696969
                android_rating_4 = 696969
                android_rating_3 = 696969
                android_rating_2 = 696969
                android_rating_1 = 696969

            res = soup.findAll("div", {"itemprop": "fileSize"})
            
            try:
                android_file_size_initial = res[0].string
                android_file_size = int(re.sub('[^0-9]','', android_file_size_initial))
            except:
                android_file_size = 696969
            
            x += 1

            #================================================================================
            #ios    
            if y == 21:
                r = open('pokemon go data/2016-07-21/' + str(files_21[x]), 'r')
            elif y == 22:
                r = open('pokemon go data/2016-07-22/' + str(files_22[x]), 'r')
            elif y == 23:
                r = open('pokemon go data/2016-07-23/' + str(files_23[x]), 'r')
            elif y == 24:
                r = open('pokemon go data/2016-07-24/' + str(files_24[x]), 'r')
            elif y == 25:
                r = open('pokemon go data/2016-07-25/' + str(files_25[x]), 'r')
            elif y == 26:
                r = open('pokemon go data/2016-07-26/' + str(files_26[x]), 'r')
            elif y == 27:
                r = open('pokemon go data/2016-07-27/' + str(files_27[x]), 'r')
            elif y == 28:
                r = open('pokemon go data/2016-07-28/' + str(files_28[x]), 'r')
            elif y == 29:
                r = open('pokemon go data/2016-07-29/' + str(files_29[x]), 'r')
            elif y == 30:
                r = open('pokemon go data/2016-07-30/' + str(files_30[x]), 'r')
            elif y == 31:
                r = open('pokemon go data/2016-07-31/' + str(files_31[x]), 'r')
                
            soup = BeautifulSoup(r, 'lxml')
    
            res = soup.findAll("span", {"class": "rating-count"})
    
            try:
                ios_current_ratings_initial = res[0].string
                ios_current_ratings = int(re.sub('[^0-9]','', ios_current_ratings_initial))
                ios_all_ratings_initial = res[1].string
                ios_all_ratings = int(re.sub('[^0-9]','', ios_all_ratings_initial))
            except:
                ios_current_ratings = 696969
                ios_all_ratings = 696969
        
    
            res = soup.findAll("ul", {"class": "list"})
            ios_file_size_holder = []
            
            for ul in res:
                for li in ul.findAll("li"):
                    for li2 in li:
                        ios_file_size_holder.append(li2.string)
            
            try:
                ios_file_size_initial = ios_file_size_holder[8]
                ios_file_size = int(re.sub('[^0-9]','', ios_file_size_initial))
            except:
                ios_file_size = 696969
                 
            dict_values = {'ios_current_ratings': int(ios_current_ratings), 'ios_all_ratings': int(ios_all_ratings),
                           'ios_file_size': int(ios_file_size), 'android_avg_rating': float(android_avg_rating),
                           'android_total_ratings': int(android_total_ratings), 'android_rating_1': int(android_rating_1),
                           'android_rating_2': int(android_rating_2), 'android_rating_3': int(android_rating_3),
                           'android_rating_4': int(android_rating_4), 'android_rating_5': int(android_rating_5),
                           'android_file_size': int(android_file_size)}
    
            dict_holder.append(dict_values)

#should be range(0,1584)
for i in range(0,1584):
	dict_holder_values = []
	for value in dict_holder[i].values():
		dict_holder_values.append(value)

	if 696969 not in dict_holder_values:
		final_dict[dates[i]] = dict_holder[i]

panda_dataframe = pd.DataFrame.from_dict(final_dict, orient = 'index')

panda_dataframe.to_csv('data.csv')
panda_dataframe.to_excel('data.xlsx')

