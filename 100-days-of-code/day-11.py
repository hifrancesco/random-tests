### continue, pass, break ###
vegetables = ["carrot", "tomato", "broccoli", "potato", "spinach"]

for veg in vegetables:
    if veg == "tomato":
        continue
    elif veg == "spinach":
        pass
    elif veg == "potato":
        break
    else:
        print(veg)