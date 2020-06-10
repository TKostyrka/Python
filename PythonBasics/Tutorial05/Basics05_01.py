from airtravel import Flight, Aircraft

f = Flight("KO1234")
a = Aircraft("G-EUPT", "Airbus A333", 22, 6)

print(a.registration())
print(a.seating_plan())
