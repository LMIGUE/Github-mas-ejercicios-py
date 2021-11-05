file = open ("devices.txt", "a")
while True:
    NewItem = input("Enter device name: ")
    if NewItem == "quit":
        print("All done!")
    break
file.write(NewItem + "\n")
file.close()

