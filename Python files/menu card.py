menu={'Idly':25,'Roti':30,'Dosa':30,'Gaare':25,'Chapathi':25,
      'Plate Meals':50,'Full Meals':70,
      'Pulihora':30,'Noodles':40,'Fried Rice':40,'Any Cool Drink':30,'Tea':10,'Coffee':15}
print("Items Available...\n")
for items,prices in menu.items():
    print(items,"Rs.",prices,'/-')
    
bill=0
order=input("Give your order : ").split(",")
for item in order:
    if item in menu.keys():
        bill+=menu[item]
    else:
        print("Item not available.",item)
print("Total bill =",'Rs.',bill,'/-')
