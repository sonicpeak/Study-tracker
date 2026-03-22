sessions = []

while True:
    print("\n1. Add Study Session")
    print("2. View Total Time")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        subject = input("Enter subject: ")
        time = float(input("Enter time studied (hours): "))
        sessions.append((subject, time))
        print(f"Added: {subject} for {time} hrs")

    elif choice == "2":
        total = 0

        if len(sessions) == 0:
            print("No sessions yet")
        else:
            print("Your sessions include:")

            for s in sessions:
                print("Subject:", s[0], "for", s[1], "hrs")
                total += s[1]

            print(f"Total time studied is {total} hrs")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")