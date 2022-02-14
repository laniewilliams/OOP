import RetailItemClass as ri

def main():
    
    descr = ['Jacket','Designer Jeans', 'Shirt']
    units = [12, 40, 20]
    p = [59.95, 34.05, 24.95]

    item1 = ri.RetailItem(descr[0],units[0],p[0])
    item2 = ri.RetailItem(descr[1],units[1],p[1])
    item3 = ri.RetailItem(descr[2],units[2],p[2])
 
    
    item1.set_description(descr[0])
    item2.set_description(descr[1])
    item3.set_description(descr[2])
    item1.set_units(units[0])
    item2.set_units(units[1])
    item3.set_units(units[2])
    item1.set_price(p[0])
    item2.set_price(p[1])
    item3.set_price(p[2])
 

    print("Item 1: ",item1.get_description(), item1.get_units(), item1.get_price())
    print("Item 2: ",item2.get_description(), item2.get_units(), item2.get_price())
    print("Item 3: ",item3.get_description(), item3.get_units(), item3.get_price())

main()