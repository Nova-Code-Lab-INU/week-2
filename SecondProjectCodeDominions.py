# --- NOVA LAB CONSOLIDATED SYSTEM ---

while True:
    print("\n" + "="*30)
    print("--- MAIN MENU ---")
    print("1. Individual Award (Badge Calculation)")
    print("2. Team Batch Process (Average Score)")
    print("3. System Status")
    print("E. Exit")
    print("="*30)
    
    choice = input("Choose option: ").strip().upper()

    # --- OPTION 1: INDIVIDUAL AWARD (Updated with logic from Code 2) ---
    if choice == "1":
        full_name = input("Enter Full Name: ").strip().title() 
        birth_year = int(input("Enter Birth Year: "))
        team_name = input("Enter Team Name: ").upper() 
        
        score = float(input("Enter Initial Tech Score (0-100): "))

        # Validation (Ensures score is in range)
        if score < 0 or score > 100:
            print("\n>> Invalid Score! Please try again with a score between 0-100.")
            continue

        # Data processing (The calculations from your second code)
        current_age = 2026 - birth_year
        system_id = len(full_name)
        potential_score = score ** 1.1
        seat_type = "Even" if system_id % 2 == 0 else "Odd"

        # Badge Logic
        if 90 <= score <= 100:
            badge = "Gold Badge"
        elif 75 <= score <= 89:
            badge = "Silver Badge"
        elif 50 <= score <= 74:
            badge = "Bronze Badge"
        else:
            badge = "Referral"

        # Final Report Output
        print(f"\n--- DIGITAL ID REPORT ---")
        print(f"Name:\t{full_name}\t(Type: {type(full_name)})")
        print(f"Team:\t{team_name}")
        print(f"Age:\t{current_age}\t(Type: {type(current_age)})")
        print(f"ID:\t{system_id}\t(Seat: {seat_type})")
        print(f"Potential:\t{potential_score:.2f}")
        print(f"Status:\t{badge}")

    # --- OPTION 2: TEAM PROCESS (Added from Code 2) ---
    elif choice == "2":
        num_members = int(input("How many members in the team? "))
        total_score = 0
        
        for i in range(1, num_members + 1):
            m_score = float(input(f"Enter score for member {i}: "))
            
            if m_score < 0 or m_score > 100:
                print("Invalid score skipped!")
                continue 
            
            total_score += m_score
        
        if num_members > 0:
            average = total_score / num_members
            print(f"\nTeam Average Score: {average:.2f}")
        else:
            print("No members entered.")

    # --- OPTION 3: SYSTEM STATUS ---
    elif choice == "3":
        print("\nSystem Status: Online")
        print("Lab Configuration: Nova Code Lab INU")

    # --- EXIT ---
    elif choice == "E":
        print("Shutting down the console... Goodbye!")
        break 

    else:
        print("Invalid Option. Please try again.")
