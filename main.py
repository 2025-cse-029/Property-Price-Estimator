from estimator import estimate_price


area = float(input("Enter house area in marla: "))
rooms = int(input("Enter number of bedrooms: "))
location = input("Enter location (central, normal, outer): ").lower()
condition = input("Enter condition (good, average, poor): ").lower()

price = estimate_price(area, rooms, location, condition)

if price is None:
    print("Invalid input")
else:
    print("Estimated price:", round(price), "PKR")
