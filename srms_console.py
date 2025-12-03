from srms_db import SRMSDB

class SRMSApp:
    def __init__(self):
        self.db = SRMSDB()

    def run(self):
        while True:
            print("\n=== SCHOOL RESULT MANAGEMENT SYSTEM ===")
            print("1. Add Student")
            print("2. Add Subject")
            print("3. Record Score")
            print("4. View Student Result")
            print("5. List Students")
            print("6. List Subjects")
            print("7. Export to CSV")
            print("0. Exit")
            c=input("Choose: ")

            if c=="1": self.add_student()
            elif c=="2": self.add_subject()
            elif c=="3": self.record_score()
            elif c=="4": self.view_result()
            elif c=="5": self.list_students()
            elif c=="6": self.list_subjects()
            elif c=="7": self.export_csv()
            elif c=="0": break
            else: print("Invalid.")

    def add_student(self):
        n=input("Student name: ")
        c=input("Class: ")
        print("ID:", self.db.add_student(n,c))

    def add_subject(self):
        n=input("Subject: ")
        r=self.db.add_subject(n)
        print("Added!" if r else "Already exists.")

    def record_score(self):
        s=int(input("Student ID: "))
        sub=int(input("Subject ID: "))
        sc=int(input("Score: "))
        print("Saved!" if self.db.record_score(s,sub,sc) else "Error.")

    def view_result(self):
        s=int(input("Student ID: "))
        r=self.db.get_student_results(s)
        if not r: print("Not found."); return
        name,cls=r["student"]
        print(f"\nResult for {name} ({cls})")
        for subj,score in r["scores"]: print(subj,":",score)
        print("Total:",r["total"])
        print("Average:",r["average"])
        print("Grade:",r["grade"])

    def list_students(self):
        for s in self.db.list_students():
            print(s[0], s[1], "(",s[2],")")

    def list_subjects(self):
        for s in self.db.list_subjects():
            print(s[0], s[1])

    def export_csv(self):
        print("Exported to:", self.db.export_results_csv())

if __name__=="__main__":
    SRMSApp().run()
