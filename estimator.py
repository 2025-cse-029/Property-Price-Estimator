base_rate = 1000000

location_rules = {
    "central": 1.2,
    "normal": 1.0,
    "outer": 0.85
}

condition_rules = {
    "good": 1.1,
    "average": 1.0,
    "poor": 0.9
}


def estimate_price(area, rooms, location, condition):
    if area <= 0 or rooms < 0:
        return None
    if location not in location_rules or condition not in condition_rules:
        return None

    price = area * base_rate
    price = price * location_rules[location]
    price = price * condition_rules[condition]
    price = price + rooms * 200000
    return round(price)
