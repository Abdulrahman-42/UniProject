import json
from datetime import datetime

class ExamHallSystem:
    def __init__(self):
        # Load data from JSON files
        with open('student_accounts.json', 'r') as f:
            self.student_accounts = json.load(f)
        
        with open('exam_halls.json', 'r') as f:
            self.exam_halls = json.load(f)

    def login(self):
        print("\n=== Exam Hall Finder System ===")
        student_id = input("Enter your Student ID: ")
        password = input("Enter your password: ")

        # Check credentials against student_accounts
        for account in self.student_accounts['accounts']:
            if account['id'] == student_id and account['password'] == password:
                return student_id
        return None

    def find_student_hall(self, student_id):
        # Search through halls to find student's assigned hall
        for hall in self.exam_halls['halls']:
            if student_id in hall['Students']:
                return hall['hall_name'], hall['location']
        return None, None

    def display_exam_schedule(self, student_id):
        hall_name, location = self.find_student_hall(student_id)
        
        if hall_name:
            print(f"\nWelcome, Student {student_id}!")
            print("\nYour Exam Hall Assignment:")
            print("-" * 50)
            print(f"Hall: {hall_name}")
            print(f"Location: {location}")
            print("-" * 50)
        else:
            print("\nNo exam hall assignment found for your ID.")

def main():
    system = ExamHallSystem()
    
    while True:
        student_id = system.login()
        if student_id:
            system.display_exam_schedule(student_id)
        else:
            print("\nInvalid credentials. Please try again.")
        
        choice = input("\nDo you want to try again? (y/n): ")
        if choice.lower() != 'y':
            print("Thank you for using Exam Hall Finder System!")
            break

if __name__ == "__main__":
    main()
