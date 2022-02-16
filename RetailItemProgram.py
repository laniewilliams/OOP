import RetailItemClass as ri


    
descr = ['Jacket','Designer Jeans', 'Shirt']
units = [12, 40, 20]
p = [59.95, 34.05, 24.95]


item1 = ri.RetailItem(descr[0],units[0],p[0])
item2 = ri.RetailItem(descr[1],units[1],p[1])
item3 = ri.RetailItem(descr[2],units[2],p[2])



print("Item 1: ","Description:",item1.get_description(),", Units in Inventory: ",item1.get_units(), ", Price: $",item1.get_price())
print("Item 2: ","Description:",item2.get_description(),", Units in Inventory: ",item2.get_units(), ", Price: $",item2.get_price())
print("Item 3: ","Description:",item3.get_description(),", Units in Inventory: ",item3.get_units(), ", Price: $",item3.get_price())

