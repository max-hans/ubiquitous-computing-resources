distance = 15  # simulated sensor value in cm

if distance < 10:
    print("sehr nah")
elif distance < 30:
    print("mittel")
else:
    print("weit weg")
