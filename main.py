from solution_1 import heroes_request, find_most_int
from solution_2 import YaUploader
from solution_3 import find_questions
from pprint import pprint

#---------------------задание 1 ---------------------
super_heroes = heroes_request()
name_list = ['Hulk', 'Captain America', 'Thanos']
name, stat = find_most_int(super_heroes, name_list)
pprint('{} with stat = {} is most intelligence hero!'.format(name, stat))
#---------------------задание 2 ---------------------

TOKEN = '' #токен сюда
uploader = YaUploader(token=TOKEN)
uploader.upload_file_to_disk('test1.txt', 'test.txt') #1 параметр назначение, 2 исходный файл.
#---------------------задание 3 ---------------------
pprint(find_questions())