"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] = max(0, inventory[item] - 1)
    return inventory


def remove_item(inventory, item):
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory):
    return [(k, v) for k, v in inventory.items() if v > 0]
