# Final Capstone Project - Database Logic
# This module synthesizes functions, lists, dictionaries, searching algorithms, and complexity analysis.

# Global Database (List of Dictionaries)
students_db = []

def add_student(student_id, name, grade):
    """
    Adds a new student to the database.
    Time Complexity: O(1) amortized, because appending to a list is constant time.
    Space Complexity: O(1) additional space (we are just appending a dict).
    """
    # Create the dictionary (Day 4 concepts)
    new_student = {
        "id": student_id,
        "name": name,
        "grade": grade
    }
    students_db.append(new_student)
    
    # After adding, we sort the database by ID to ensure Binary Search works later.
    # Time Complexity of sort: O(N log N)
    students_db.sort(key=lambda s: s["id"])
    return True

def search_student_by_name(name):
    """
    Finds a student using Linear Search.
    Time Complexity: O(N) because the database is sorted by ID, not by name.
    Space Complexity: O(1)
    """
    # Linear Search logic (Day 7 concepts)
    for student in students_db:
        if student["name"].lower() == name.lower():
            return student
    return None

def search_student_by_id(target_id):
    """
    Finds a student using Binary Search.
    Time Complexity: O(log N) because the database is already sorted by ID.
    Space Complexity: O(1) iterative space.
    """
    low = 0
    high = len(students_db) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_student = students_db[mid]
        mid_id = mid_student["id"]
        
        if mid_id == target_id:
            return mid_student
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
            
    return None

def get_all_students():
    """
    Returns all students.
    Time Complexity: O(1) to return the reference.
    """
    return students_db

def clear_database():
    """
    Helper for testing to clear out global state.
    """
    global students_db
    students_db = []
