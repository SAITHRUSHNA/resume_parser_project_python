resume = "Name: Sai THRUSHNA\nSkills: python, java, SQL, Python\nExperience:2years\nCGPA:8.54"

# Step 1: Clean and Normalize Resume Text
resume = resume.lower().strip()         # Lowercase and remove outer spaces
lines = resume.split("\n")              # Split by newline

# Step 2: Convert to Dictionary
resume_data = {}
for line in lines:
    key, value = line.split(":", 1)     # Split at first colon only
    resume_data[key.strip()] = value.strip()

# Step 3: Convert Skills String to List
skills_list = resume_data["skills"].split(",")               # Split skills by comma
skills_list = [skill.strip() for skill in skills_list]       # Clean each skill

# Step 4: Convert Skill List to Set (Remove Duplicates)
unique_skills = set(skills_list)

# Step 5: Store All Resume Data as Tuple in a List
all_resumes = [
    ("Rahul", {"skills": {"python", "sql"}, "cgpa": 8.1}),
    ("Nehaa", {"skills": {"java", "ml"}, "cgpa": 8.7}),
    ("Amit", {"skills": {"python", "java"}, "cgpa": 7.9}),
    ("Sai", {"skills": unique_skills, "cgpa": float(resume_data["cgpa"])})  # Add Sai's resume
]

# Step 6: Filter Students Having 'python' Skill
python_students = [name for name, data in all_resumes if "python" in data["skills"]]
print("Students Knowing Python:", python_students)

# Step 7: Sort Students by CGPA
sorted_students = sorted(all_resumes, key=lambda x: x[1]["cgpa"], reverse=True)
print("Topper:", sorted_students[0])  # Student with highest CGPA

# Step 8: Find Common Skills (skills shared by all students)
all_skills = [data["skills"] for _, data in all_resumes]
common_skills = set.intersection(*all_skills)
print("Common Skills:", common_skills)

# Step 9: Group Students by Skill
skill_groups = {}
for name, data in all_resumes:
    for skill in data["skills"]:
        if skill not in skill_groups:
            skill_groups[skill] = set()
        skill_groups[skill].add(name)

# Helper function for union of all skill sets
def set_union(*sets):
    return set().union(*sets)

# Step 10: Print Summary Report
print("\n--- Resume Summary Report ---")
print("Total Students:", len(all_resumes))
print("Skills Covered:", set_union(*all_skills))
print("Students per Skill:")
for skill, group in skill_groups.items():
    print(f"{skill.title()}: {len(group)} student(s)")
