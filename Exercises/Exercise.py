def item_order(order):
    order_dict = {"salad": 0, "hamburger": 0, "water": 0}
    order = str(order)
    items = order.split()

    for item in items:
        order_dict[item] += 1

    return str("salad:" + str(order_dict['salad'])
               + " hamburger:" + str(order_dict['hamburger'])
               + " water:" + str(order_dict['water']))

print item_order('')
print item_order('hamburger')
