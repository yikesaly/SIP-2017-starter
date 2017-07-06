start = '''
Summer's here, and it's time for a vacation!
'''
print(start)

print("Choose a character to begin: Scott, Kami, or Taylor")
character = input()
if character == "Scott":
    print("You're going to Hawaii!")
elif character == "Kami":
    print("You're going to Italy!")
elif character == "Taylor":
    print("You're going to Korea!")
else:
    print("Incorrect input! Try again")


print("Do you want to pack or go straight to the airport?")

where = input()
if where == "pack":
    if character == "Scott":
        print("You pack clothes, soda, and chips.")
    if character == "Kami":
        print("You pack toiletries, shoes, electronics, and clothes.")
    if character == "Taylor":
        print("You pack lots of makeup, clothes, shoes, and snacks.")
    print("You leave the house and go to the airport.")
    print("You check in and the employees scan your luggage.")
    if character == "Scott":
        print("You have too much soda in your luggage! Do you want to throw it away or cancel your trip?")
        soda = input()
        if soda == "throw it away":
            print("You board the plane and arrived in Hawaii!")
        if soda == "cancel your trip":
            print("You go home.")

    if character == "Kami":
        print("You packed way too much! Would you want to pay a fee or cancel your trip?")
        clothes = input()
        if clothes == "pay a fee":
            print("You board the plane and arrived in Italy!")
        if clothes =="cancel your trip":
            print("You go home.")

    if character == "Taylor":
        print("You packed liquid makeup! Would you like to throw it away or cancel your trip?")
        makeup = input()
        if makeup == "throw it away":
            print("You board the plane and arrived in Korea!")
        if makeup == "cancel your trip":
            print("You go home.")

if where == "go straight to the airport":
    print("You arrive at the airport and realize you forgot your passport! Go home.")
