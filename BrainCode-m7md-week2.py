################Project week 2##################
################################################

print("---------------Welcom to BrainCode team---------------")

################1-Authentication Module (The Security Gate)#########################

while True:
    username=input("Enter user name: ")
    code=input("Enter access code: ")
    
    if username=="admin"and code=="admin":
         print("Access Granted ")
         break
    else:
         print("Access Denied ")
         print("Please enter a valid value ")

################2-The Command Center (Persistent UI)#########################

print("\n###########MENU###########")
print("1-Individual Award")
print("2-Team Process")
print("3-System Status")
print("E-Exit")

choice=input("choose option: ").strip().upper()

################3-Decision Engine (Badge Classification)#########################

if choice=='1':
    score=float(input("Enter student score: "))
    if score < 0 or score > 100:
        print("Invalid value")
    elif score >= 90:
        print("Gold Badge")
    elif score >= 75:
        print("Silver Badge")
    elif score >= 50:
        print("Bronze Badge")
    else:
        print("Referral")

################4-Team Analytics Module (The For-Loop)#########################

elif choice == "2":
    members = int(input("Enter number for members :"))
    total = 0 
   
    for i in range(members):
        score = float(input(f"Enter number for member {i+1} :"))
        
        if score < 0 or score > 100 :
            print("Invalid score , skipped")
            continue 
        total += score
    if members > 0 :
        average = total / members
        print(f"Team Average = {average}")
        
################5-System Integrity (Validation & Control)#########################
        
elif choice == "3":
   
    print("system is running normally")

################6-Professional Formatting#########################

elif choice=="E":
    while True:
       print("Exiting system")
       break 
else:
  print("invalid choice")