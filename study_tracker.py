import json

# Load existing sessions from file
try:
    with open("sessions.json", "r") as f:
        sessions = json.load(f)
except:
    sessions = []

while True:
    print("\n1. Add Study Session")
    print("2. View Total Time")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        subject = input("Enter subject: ")
        time = float(input("Enter time studied (hours): "))

        
        sessions.append({"subject": subject, "time": time})

        # Saveing to file immediately
        with open("sessions.json", "w") as f:
            json.dump(sessions, f)

        print("Session added")

    elif choice == "2":
        total = 0

        if len(sessions) == 0:
            print("No sessions yet")
        else:
            print("Your sessions include:")

            for s in sessions:
                print("Subject:", s["subject"], "for", s["time"], "hrs")
                total += s["time"]

            print("Total time studied is", total, "hrs")

    elif choice == "3":
        break

    else:
        print("Invalid choice")