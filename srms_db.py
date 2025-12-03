import sqlite3
import csv

class SRMSDB:
    def __init__(self, db_name="srms_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.init_db()

    def init_db(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, class_name TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS subjects(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS scores(id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, subject_id INTEGER, score INTEGER, UNIQUE(student_id, subject_id))")
        self.conn.commit()

    def add_student(self, name, class_name):
        self.cursor.execute("INSERT INTO students(name, class_name) VALUES(?,?)",(name,class_name))
        self.conn.commit()
        return self.cursor.lastrowid

    def list_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def add_subject(self, name):
        try:
            self.cursor.execute("INSERT INTO subjects(name) VALUES(?)",(name,))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            return None

    def list_subjects(self):
        self.cursor.execute("SELECT * FROM subjects")
        return self.cursor.fetchall()

    def record_score(self, student_id, subject_id, score):
        if not (0 <= score <= 100): return False
        try:
            self.cursor.execute("INSERT OR REPLACE INTO scores(student_id, subject_id, score) VALUES(?,?,?)",(student_id,subject_id,score))
            self.conn.commit()
            return True
        except:
            return False

    def get_student_results(self, student_id):
        self.cursor.execute("SELECT name, class_name FROM students WHERE id=?",(student_id,))
        student = self.cursor.fetchone()
        if not student: return None
        self.cursor.execute("SELECT subjects.name, scores.score FROM scores JOIN subjects ON scores.subject_id=subjects.id WHERE scores.student_id=?",(student_id,))
        results = self.cursor.fetchall()
        if not results:
            return {"student": student, "scores": [], "total": 0, "average": 0, "grade": "N/A"}
        total = sum(r[1] for r in results)
        avg = total / len(results)
        grade = self._grade(avg)
        return {"student": student, "scores": results, "total": total, "average": round(avg,2), "grade": grade}

    def _grade(self, avg):
        if avg>=70: return "A"
        if avg>=60: return "B"
        if avg>=50: return "C"
        if avg>=45: return "D"
        return "F"

    def export_results_csv(self, filename="results_export.csv"):
        self.cursor.execute("SELECT students.name, students.class_name, subjects.name, scores.score FROM scores JOIN students ON scores.student_id=students.id JOIN subjects ON scores.subject_id=subjects.id")
        data = self.cursor.fetchall()
        import csv
        with open(filename,"w",newline="") as f:
            w=csv.writer(f)
            w.writerow(["Student","Class","Subject","Score"])
            w.writerows(data)
        return filename
