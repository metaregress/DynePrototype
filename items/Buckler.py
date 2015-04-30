import Item
import json

def Buckler():
    with open('items/buckler.json') as data_file:
        buckler_dict = json.load(data_file)
        buckler_item = Item.Item(buckler_dict)        
    return buckler_item
