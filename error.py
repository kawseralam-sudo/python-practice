try:
    with open("data.txt","r") as file:
        data=file.read()
        print(data)
except FileNotFoundError:
    print("data not found")