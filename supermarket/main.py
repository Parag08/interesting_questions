import math

inventory_dict = {
    "Apple": {
        "price":50,
        "Percent_discounts":[10,18],
        "numeric_discounts":[[3,1]]
    },
    "Orange": {
        "price":80,
        "Percent_discounts":[10,18,20],
        "numeric_discounts":[]
    },
    "Potato": {
        "price":30,
        "Percent_discounts":[10,5],
        "numeric_discounts":[[5,2]]
    },
    "Tomato": {
        "price":70,
        "Percent_discounts":[10,5,10],
        "numeric_discounts":[]
    },
    "Cow Milk": {
        "price":50,
        "Percent_discounts":[15,20],
        "numeric_discounts":[[3,1]]
    },
    "Soy Milk": {
        "price":40,
        "Percent_discounts":[15,20,10],
        "numeric_discounts":[]
    },
    "Cheddar": {
        "price":50,
        "Percent_discounts":[15,20],
        "numeric_discounts":[[2,1]]
    },
    "Gouda": {
        "price":80,
        "Percent_discounts":[15,20,10],
        "numeric_discounts":[]
    }
}

#item_array = input().split(',')
item_array = "Apple 6Kg, Orange 2Kg, Potato 14Kg, Tomato 3Kg, Cow Milk 8Lt, Gouda 2Kg".split(',')

for item in item_array:
    name = ' '.join(item.split()[0:-1])
    quantity = int(item.split()[-1][0:-2])
    item_object = inventory_dict[name]
    price = item_object["price"]
    max_percentage_discount = max(item_object["Percent_discounts"])
    max_numeric_discount = None
    for numeric_discount in item_object["numeric_discounts"]:
        if len(numeric_discount) < 3:
            numeric_discount.append(numeric_discount[1] + numeric_discount[0])
            numeric_discount.append(numeric_discount[1]*100/numeric_discount[2])
        if (numeric_discount[3] > max_percentage_discount) and (max_numeric_discount == None):
            max_numeric_discount = numeric_discount
        if (max_numeric_discount != None) and (numeric_discount[3] > max_numeric_discount[3]):
            max_numeric_discount =  numeric_discount
    if max_numeric_discount != None:
        quantity_from_numeric_discount = int(quantity/max_numeric_discount[2])*max_numeric_discount[2]
        quantity_from_max_discount = quantity - quantity_from_numeric_discount
        f_price = quantity_from_numeric_discount*price*(1-(max_numeric_discount[3]/100)) + quantity_from_max_discount*price
    else:
        f_price = quantity*price*(1 - (max_percentage_discount/100))
    print(item,int(f_price))