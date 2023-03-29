

# with open('weather_data.csv') as weather_data:
#   data = weather_data.readlines()
#   print(data)



# import csv

# with open('weather_data.csv') as data_file:
#   data = csv.reader(data_file)
#   temperature = []
#   for row in data:
#     if row[1] != 'temp':
#       temperature.append(int(row[1]))
#   print(temperature)


import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

"""convert data to dictionary"""
# data_dict = data.to_dict()
# print(data_dict)

"""Convert the 'temp' section into list and then calculate the average"""
# temp_list = data['temp'].to_list()
# average = sum(temp_list) / len(temp_list)
# print(int(average))

"""Directly get the average of the 'temp' section"""
# average = data['temp'].mean()
# max_temp = data['temp'].max()
# print(average)

"""Directly get the maximum temperature of the 'temp' section"""
# temp_list = data['temp'].to_list()
# max_temp = pandas.Series(temp_list).max()
# print(max_temp)

"""Get the row"""
# row = data[data.day == 'Monday']
# print(row)


"""Get the row of data that has the maximun temperature"""
# row = data[data.temp == data.temp.max()]
# print(row)

"""Convert the temperature of day 'Monday' from celcius to fahrenheit"""
# monday = data[data.day == 'Monday']
# temp_fahrenheit = (monday.temp * 1.8) + 32
# print(temp_fahrenheit)

"""Create a dataFrame from scratch"""
# data_dic = {
#   "students": ['Amy', 'James', 'Angela'],
#   "scores": [76, 65, 80]
# }

# data = pandas.DataFrame(data_dic)
# data.to_csv('new_data.csv')

"""My version"""

# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# # print(data['Primary Fur Color'])
# data_list = data['Primary Fur Color'].to_list()
# # print(data_list)
# gray = []
# cinnamon = []
# black = []
# for color in data_list:
#   if color == 'Gray':
#     gray.append(color)
#   elif color == 'Cinnamon':
#     cinnamon.append(color)
#   elif color == 'Black' :
#     black.append(color)
    
# data_dic = {
#   'Fur Color' : [ 'Gray', 'Cinnamon', 'Black' ],
#   'Count' : [ len(gray), len(cinnamon), len(black) ]
# }

# data = pandas.DataFrame(data_dic)
# data.to_csv('squirrel_count.csv')


"""Tutor Version"""
# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# gray_color_count = len(data[data['Primary Fur Color'] == 'Gray'])
# cinnamon_color_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# black_color_count = len(data[data['Primary Fur Color'] == 'Black'])

# data_dict = {
#   'Fur Color' : [ 'Gray', 'Cinnamon', 'Black' ],
#   'Count' : [ gray_color_count, cinnamon_color_count, black_color_count ]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv('squirrel_count.csv')

# print(f'{gray_color_count}\n{cinnamon_color_count}\n{black_color_count}')