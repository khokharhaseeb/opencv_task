import json
import os


folder = 'id_card_data'
 
def save_data(dic):
    if not os.path.exists(folder):
        os.makdir(folder)
    if dic['Identity Number'] != '-':
        path = fr'{folder}/{dic["Identity Number"]}.json'
        with open(path, "a+") as outfile:
            json.dump(dic, outfile)
    
def check_file(name):
    path = fr'{folder}/{name}.json'
    if os.path.exists(path):
        f = open(path)
        data = json.load(f)
    return data
    
