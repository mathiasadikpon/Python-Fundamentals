inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def  print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches

    print(f"Total snowfall inches: {total_inches}")


# Call the function to print the total snowfall
print_total_snowfall(inches_snow)

try:
    # Snowfall on Thursday
    inches_thursday = int(input("How many inches of snow fell on Thursday? "))
    inches_snow["Thursday"] = inches_thursday
    
    # Call the function again to print the updated total snowfall
    print_total_snowfall(inches_snow)
except:
    print("Invalid input. Please enter a number.")

