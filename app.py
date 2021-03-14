q = ""
while q.lower() != "q":
    print("\t\tWELCOME to kg -> lbs & lbs -> kg converter ")

    name = input("What's your name? ")
    print(f"Hello {name}")

    print("--- --- --- --- --- --- --- --- --- --- --- --- ---")

    invalid = True
    while invalid:
        try:
            weight = float(input("Please enter your weight: "))
            if weight < 5:
                print("Is it possible to be so lite?")
            elif weight > 500:
                print("That's a lot!")
            else:
                invalid = False
        except:
            print("Wrong input.")

    print("---------------------------------------")

    print("In which unit is your weight? ")
    invalid_2 = True
    while invalid_2:
        try:
            unit = int(input("For kg type 1\nFor lbs type 2: "))
            invalid_2 = False
            while ((unit != 1) and (unit != 2)):
                unit = int(input("Please enter 1 for kg\nand 2 for lbs: "))
        except:
            print("Wrong input.")

    print("---------------------------------------")

    if unit == 1:
        weight_lbs = weight * 2.20462
        print(f"{name}'s weight is: {weight_lbs} lbs")
    elif unit == 2:
        weight_kg = weight / 2.20462
        print(f"{name}'s weight is: {weight_kg} kg")
    else:
        print("Please use a valid unit...")

    q = input('If you want to quit press "N" or press enter to convert again: ')

print("......................................")
print(f"Thank you {name}")
input("Press Enter ")
