#login phase
user_name=input("Enter User name: ")
pass_code=input("Enter Access code: ")

#verify credentials using logical and operator
if user_name =="admin" and pass_code =="1234":
   print("access granted")

#control variable for the while loop 
   status = True
#infinite loop
   while status:
      print("\n--- NOVA MENU ---")
      print ("1. Individual Award")
      print ("2. Team Batch Process")
      print ("3. System Status")
      print ("E. Exit")
      Choice = input("Select: ").strip().upper()
#individual award
      if choice == "1":
          score= float (input("Enter student score: "))
          if score>= 0 and score<= 100:
             if score>= 90:
               badge="Gold"
             elif score >= 75:
               badge= "Silver"
             elif score >= 50 :
               badge= "Bronze"
             else:
               badge= "Referral"
             print("badge Assigned: " +  badge)
          else:
            print("Invalid Score! Please enter 0_100")

#team batch process
      elif choice =="2": 
        members=int(input("How many mrmbers?"))
        total=0
        count=0
    
      for i in range (members):
          s=float(input("Enter score for member:"))
          if s<0 or s>100:
             print("Out of range ,skipping")
             continue
          total=total+s
          count=count+1
#calculate the team avarge 
      if count >0:
         average = total / count 
         print ("Team average is: ")
         print(average)
    #system status
      elif choice =="3":
        print ("system status : All Labs Operational")
    #exit option
      elif choice=="E":
        print("shutting down ")
        status=False
      else:
        print("unknown command , try again .")
#erorr massage
else:
  print("login failed")


