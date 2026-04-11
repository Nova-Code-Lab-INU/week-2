# add students

students = []
Username = input("Enter your name: ").strip()
Password = input("Enter your password: ").strip()

# checking if the username and password are not empty and printing a welcome message if they are valid, otherwise printing an error message

if Username and Password:
    student = {"Name": Username, "Password": Password ,"points" : 0 }
    students.append(student)
    print(f"Welcome to the system, {Username}!")
else:
    print("Invalid username or password. Please try again.")

print("Current students:", students)

while True:
    print("\n ---Commend Center--- ")
    print("[1] Individual Award")
    print("[2] Team Batch Process")
    print("[3] System Status")
    print("[E] Exit System")

    Choice = input("Enter your choice:").strip().upper()

    
    if Choice == "1":
        Score = int (input("Enter the score :"))

        if Score < 0 or Score > 100:
            print ("Invalid score")
            continue

        if Score >= 90:
           badge = "Gold"
        elif Score >= 80:
            badge = "Silver"
        elif Score >= 70:
            badge = "Bronze"
        else:
            badge = "No badge"


    elif Choice == "2":
        members = int(input("Enter the number of team members:"))
        total = 0
        valid_members = 0

        for i in range(members):
            Score = int(input(f"Enter the score for member {i+1}:"))
            if Score < 0 or Score > 100 :
                print ("Invalid score")
                continue

            total += Score
            valid_members += 1

        if valid_members > 0:

            Average = total / valid_members
            print (f"The total score for the team : {total} and the average score : {Average}")
        else:
            print(" no valid scores")

    elif Choice == "3":
        print(" \n system status:")
        print("System is running Normally ")
        print("NO issuss detected")

    elif Choice.upper() == "E":
        print ("Exiting the system. ")
        break
    else:
        print("Invalid choise.")

print(f"{Username}: {student['points']} - {badge}")


team_name = input("Enter your team name:")
members = int(input("Enter the number of team members:"))

while True:
    team_name = input("enter your team name :")
    if team_name == "exit":
        print("Exiting the system:")
        break
    else :
        print(f"team '{team_name}' is registered successfully")