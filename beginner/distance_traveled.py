#!/usr/bin/python3

# User input for time
print("Enter Time:", end=" ")
Hrs = float(input("Hours: "))
Min = float(input("Minutes: "))
Sec = float(input("Seconds: "))

# Time conversion
t = []
t.append(Hrs * 3600)
t.append(Min * 60)
t.append(Sec)
time = float(sum(t) / 3600)

# Distance calculation
s = 70
d = s * time

# Display
print(f"Distance traveled: {d:.2f} miles")

