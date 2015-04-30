import json
import Item

def HideArmor():
    with open('items/hidearmor.json') as data_file:
        hide_armor_dict = json.load(data_file)
        hide_armor_item = Item.Item(hide_armor_dict)
        return hide_armor_item
