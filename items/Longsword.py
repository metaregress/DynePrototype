import json
import Item

def Longsword():
    with open('items/longsword.json') as data_file:
        longsword_dict = json.load(data_file)
        longsword_item = Item.Item(longsword_dict)

    return longsword_item
