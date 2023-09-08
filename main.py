try:
    with open("filename1.json") as f:
        st = f.read()
except FileNotFoundError as e:
    print("The file did not found: " + str(e))

print("Hello World")