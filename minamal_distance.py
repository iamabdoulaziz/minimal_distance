

drivers_name = ["Sycasso", "Bamby", "Cute boy", "Alienne", "Super sayenne", "Z-hero", "Hero"]
driver_distance_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

"""
min_distance = driver_distance_km[0]
distance_index = 0
for distance in driver_distance_km:
    if distance < min_distance:
        min_distance = distance
        distance_index = driver_distance_km.index(min_distance)
        indexing_driver = drivers_name[distance_index]
        print(f"Le nom du chauffeur le plus proche est : {indexing_driver}")

print(f"La distance minimale est : {min_distance} km")
print(f"L'index est : {distance_index}")
"""
driver = drivers_name[0]
min_index = 0
min_distance = driver_distance_km[0]
for i in range(len(driver_distance_km)):
    distance = driver_distance_km[i]
    if distance < min_distance:
        min_distance = distance
        min_index = i
        driver = drivers_name[i]

print(f" Distance minimal {min_distance} km")
print(f"Index de la distance minimale : {min_index}")
print(f"Le nom du chauffeur est : {driver}")
