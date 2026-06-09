import sys
from database import add_student, search_student_by_name, search_student_by_id, get_all_students

def display_menu():
    """
    Displays the CLI menu using print formatting.
    """
    print("\n" + "="*40)
    print("🎓 STUDENT DATABASE MANAGER 🎓")
    print("="*40)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by Name (Linear Search O(N))")
    print("4. Search Student by ID (Binary Search O(log N))")
    print("5. Exit")
    print("="*40)

def main():
    """
    Main loop synthesizing while loops, conditionals, and error handling.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            try:
                # Type conversion (Day 1)
                student_id = int(input("Enter Student ID (Number): "))
                name = input("Enter Student Name: ")
                grade = input("Enter Student Grade: ")
                
                add_student(student_id, name, grade)
                print(f"✅ Success! {name} was added to the database.")
            except ValueError:
                print("❌ Error: Student ID must be an integer!")
                
        elif choice == '2':
            students = get_all_students()
            if not students:
                print("📂 The database is currently empty.")
            else:
                print("\n--- Student Roster ---")
                for s in students:
                    print(f"ID: {s['id']} | Name: {s['name']} | Grade: {s['grade']}")
                    
        elif choice == '3':
            name = input("Enter name to search: ")
            result = search_student_by_name(name)
            if result:
                print(f"🎯 Found via Linear Search: ID {result['id']}, {result['name']}, Grade {result['grade']}")
            else:
                print(f"❌ Could not find a student named '{name}'.")
                
        elif choice == '4':
            try:
                target_id = int(input("Enter ID to search: "))
                result = search_student_by_id(target_id)
                if result:
                    print(f"🚀 Found via Binary Search: ID {result['id']}, {result['name']}, Grade {result['grade']}")
                else:
                    print(f"❌ Could not find a student with ID '{target_id}'.")
            except ValueError:
                print("❌ Error: Target ID must be an integer!")
                
        elif choice == '5':
            print("Goodbye! Terminating application.")
            sys.exit(0)
            
        else:
            print("❌ Invalid choice. Please select 1 through 5.")

if __name__ == "__main__":
    main()
