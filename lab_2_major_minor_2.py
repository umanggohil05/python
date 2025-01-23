def major_minor():
    age = int (input("Enter your age:"))
    if age<18:
       print("you are still minor.")
    else :
        print("You have become major ,now.")
    print("minor") if age < 18 else print("major")

major_minor()
major_minor()

