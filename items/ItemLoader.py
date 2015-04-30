import os
import json
import Item

def loadItems():
    items = {}
    for dirname, dirnames, filenames in os.walk('items'):
        for filename in filenames:
            if filename[-5:] == '.json':
                with open('items/' + filename) as data_file:
                    item_dict = json.load(data_file)
                    items[item_dict['name']] = Item.Item(item_dict)
    return items
