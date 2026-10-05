mobile =  "redmi","mi"

while True:
    guess = input("Enter the mobile name: ").lower()

    if guess in mobile:
        print("Congratulations! Yes, Kawsar Alam uses Redmi phone.")
        break
    else:
        print("Kawsar Alam does not use this phone! Try again!")