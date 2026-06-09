import unittest
import sys
import os

# Add Final_Capstone to path so we can import database
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Final_Capstone')))

from database import add_student, search_student_by_name, search_student_by_id, get_all_students, clear_database

class TestStudentDatabase(unittest.TestCase):
    
    def setUp(self):
        """Runs before every single test to ensure a clean slate."""
        clear_database()

    def test_add_student(self):
        """Test that a student is added correctly."""
        add_student(101, "Alice", "A")
        students = get_all_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "Alice")

    def test_database_is_sorted_automatically(self):
        """Test that adding students keeps the list sorted by ID for Binary Search."""
        add_student(500, "Charlie", "C")
        add_student(100, "Alice", "A")
        add_student(300, "Bob", "B")
        
        students = get_all_students()
        # Should be ordered: 100, 300, 500
        self.assertEqual(students[0]["id"], 100)
        self.assertEqual(students[1]["id"], 300)
        self.assertEqual(students[2]["id"], 500)

    def test_linear_search_by_name(self):
        """Test finding a student using linear search (O(N))."""
        add_student(101, "Alice", "A")
        add_student(102, "Bob", "B")
        
        result = search_student_by_name("Bob")
        self.assertIsNotNone(result)
        self.assertEqual(result["id"], 102)
        
        # Test case insensitivity
        result_lower = search_student_by_name("bob")
        self.assertIsNotNone(result_lower)

        # Test not found
        result_none = search_student_by_name("Charlie")
        self.assertIsNone(result_none)

    def test_binary_search_by_id(self):
        """Test finding a student using binary search (O(log N))."""
        for i in range(1, 101):
            add_student(i, f"Student_{i}", "A")
            
        # Target in the middle
        result = search_student_by_id(50)
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Student_50")
        
        # Target at the edges
        self.assertEqual(search_student_by_id(1)["name"], "Student_1")
        self.assertEqual(search_student_by_id(100)["name"], "Student_100")
        
        # Target not found
        self.assertIsNone(search_student_by_id(101))
        self.assertIsNone(search_student_by_id(0))

if __name__ == "__main__":
    unittest.main()
