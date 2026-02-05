def get_engineering_high_salary_employees(database):
    query = {
        "job_role.department": "Engineering",
        "salary": {"gt": 65000}
    }
    projection = {
        "_id": 0,
        "employee_id": 1,
        "name": 1,
        "salary": 1
    }
    employees = list(database.collection.find(query, projection))
    return employees

def get_employees_by_age_and_role(database):
    query = {
        "$and": [
            {"age": {"gte": 30}}, {"age": {"lte": 45}},
            {"$or": [{"job_role.title": "Engineer"}, {"job_role.title": "Specialist"}]}
        ]
    }
    employees = list(database.collection.find(query))
    for employee in employees:
        employee["_id"] = str(employee["_id"])
    return employees

def get_top_seniority_employees_excluding_hr(database):
    query = {
        "job_role.department": {"$ne": "HR"}
        }
    
    employees = list(database.collection.find(query, sort=("years_at_company", -1 )).limit(7))
    for employee in employees:
        employee["_id"] = str(employee["_id"])
    return employees

def get_employees_by_age_or_seniority(database):
    query = {
        "$or": [
            {"age": {"$gt": 50}},
            {"years_at_company": {"$lt": 3}}
        ]
    }
    projection = {
        "_id": 0,
        "employee_id": 1,
        "name": 1,
        "salary": 1,
        "years_at_company": 1
    }
    employees = list(database.collection.find(query, projection))
    return employees

def get_managers_excluding_departments(database):
    query = {
        {"$and":[
            {"job_role.title": "Manager"},
            {"job_role.department": {"$not": {"$in": ["Sales", "Marketing"]}}}
        ]}
    }

    employees = list(database.collection.find(query))
    for employee in employees:
        employee["_id"] = str(employee["_id"])
    return employees

def get_employees_by_lastname_and_age(database):
    query = {
        "$and": [
            {"age": {"$lt": 35}},
            {"$or": [
                {"name": {"$regex": "^Nelson"}},
                {"name": {"$regex": "^Wright"}}
            ]}
        ]
    }
    projection = {
        "_id": 0,
        "name": 1,
        "age": 1,
        "job_role.department": 1
    }
    employees = list(database.collection.find(query, projection))
    return employees