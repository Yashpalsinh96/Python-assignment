temperature_readings = [25,28,21,24,27]

if not temperature_readings:
    print("Temperature readig is empty.")

else:
    average_temp = sum (temperature_readings) / len (temperature_readings)
    print("Average Temperature: ", average_temp)

    highest_temp = max (temperature_readings)
    print("Highest Temperature: ", highest_temp)

    lowest_temp = min (temperature_readings)
    print("lowest Temperature: ", lowest_temp)