import datetime

assignments = []

def add_assignment():
    name = input("Enter assignment name: Project Report Writing ")
    due_date = input("Enter due date (2025-10-04): ")
    assignments.append({"name": name, "due_date": due_date})
    print("Assignment added!\n")

def view_assignments():
    if not assignments:
        print("No assignments found.\n")
        return
    print("Your Assignments:")
    for i, a in enumerate(assignments):
        print(f"{i+1}. {a['name']} - Due: {a['due_date']}")
    print()

def delete_assignment():
    view_assignments()
    if not assignments:
        return
    idx = int(input("Enter assignment number to delete: ")) - 1
    if 0 <= idx < len(assignments):
        removed = assignments.pop(idx)
        print(f"Removed: {removed['name']}\n")
    else:
        print("Invalid number!\n")

def alert_due_tomorrow():
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    due_tomorrow = [a for a in assignments if a['due_date'] == tomorrow]
    if due_tomorrow:
        print("⚠️  Assignments due tomorrow:")
        for a in due_tomorrow:
            print(f"- {a['name']}")
        print()
    else:
        print("No assignments due tomorrow.\n")

# Main loop
while True:
    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Delete Assignment")
    print("4. Alert for Assignments Due Tomorrow")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_assignment()
    elif choice == "2":
        view_assignments()
    elif choice == "3":
        delete_assignment()
    elif choice == "4":
        alert_due_tomorrow()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
