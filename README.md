# resume_parser_project_python
# 📌 Resume Parser Project (Python)

This is a small Python project that demonstrates how to parse and analyze resume text data.  
It shows how to:
✅ Clean and normalize text  
✅ Extract fields into a dictionary  
✅ Process and deduplicate skills  
✅ Find students who know Python  
✅ Sort students by CGPA  
✅ Find common skills among all students  
✅ Group students by skill and generate a summary report

---

## 🐍 **Technologies Used**
- Python (basic string processing & data structures)
- Lists, sets, dictionaries
- Simple filtering, sorting and grouping

---

## 📊 **What the script does**
- Parses a sample resume text and extracts data
- Builds a list of student profiles with skills & CGPA
- Filters students who know 'Python'
- Finds the student with highest CGPA
- Finds common skills shared by all students
- Groups students by skill and prints summary

---

## 🧩 **Sample Output**
```text
Students Knowing Python: ['Rahul', 'Amit', 'Sai']
Topper: ('Nehaa', {'skills': {'ml', 'java'}, 'cgpa': 8.7})
Common Skills: set()
--- Resume Summary Report ---
Total Students: 4
Skills Covered: {'python', 'java', 'ml', 'sql'}
Python: 3 student(s)
Sql: 2 student(s)
Java: 3 student(s)
Ml: 1 student(s)
