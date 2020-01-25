def carbonFootprint(milesDrove, flightHours, beefConsumed, shoppingTrips):
    #driving is the main way people travel in the US short-term
    #flying is the most common way people travel long distance
    #consumption of the beef has a higher carbon footprint than any other food
    #shopping in person produces a significant amount of CO2
    c1 = milesDrove * 14.25
    c2 = flightHours * 8818.49
    c3 = beefConsumed * 26.44
    c4 = shoppingTrips * 144
    c_total = c1 + c2 + c3 + c4
    c_total = c_total / 32000
    c_total = c_total * 12


    #print("This is how much CO2 you produce in tons in a year:", c_total, "tons")
