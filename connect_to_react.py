import mothers

def main():
    while True:
        print("welcom to our babysitter mediation site!")
        print("Please choose an option :")
        print("1 search for babysitter")
        print("2 for register babysitter")
        print("3 exit")

        choice=input(">")

        if choice=="1":
            search()

        elif choice=="2":
            register()
        elif choice=="3":
            print("thank you for using our site!")
            break
        else:
            print("invalid choice please try again")
def search():
    print("please enter your deatials")
    hours = input("Hours: ")
    days = input("Days: ")
    area = input("Area: ")

