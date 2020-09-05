# You all are pilots, you have to land a plane, the altitude required for landing a plane is 1000ft,
#if less than that tell pilot to land the plane, or it is more than that but less than 5000 ft ask pilot to
# come down to 1000ft else if it is more than 5000ft ask pilot to go around and try later!

Altitude = input("Enter the number")
Altitude = int(Altitude)

if(Altitude>=1 and Altitude <=1000):
    print("Safe to land plane from Altitude: ",Altitude)
elif(Altitude>1000 and Altitude<=5000):
    print("Altitude required for landing plane is 1000ft")
elif(Altitude>5000):
    print("Turn Around and try later")
else:
    print("Altitude value should be greater than zero")



