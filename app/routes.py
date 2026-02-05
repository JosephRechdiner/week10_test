from fastapi import APIRouter, Depends, Request, HTTPException
from dal import DalManager

employees_router = APIRouter()

# DEPENDENCIES
def get_database(request: Request):
    return request.app.state.database

# ROUTES

# 1
@employees_router.get("/employees/engineering/high-salary")
def get_employees_salary(database = Depends(get_database)):
    employees = DalManager.get_engineering_high_salary_employees(database)
    if not employees:
        raise HTTPException(status_code=404, detail=f"Not found!, Error: {str(e)}")
    return employees

# 2
@employees_router.get("/employees/by-age-and-role")
def get_employees_age_and_role(database = Depends(get_database)):
    employees = DalManager.get_employees_by_age_and_role(database)
    if not employees:
        raise HTTPException(status_code=404, detail=f"Not found!, Error: {str(e)}")
    return employees

# 3
@employees_router.get("/employees/top-seniority")
def get_employees_top_seniority(database = Depends(get_database)):
    employees = DalManager.get_top_seniority_employees_excluding_hr(database)
    if not employees:
        raise HTTPException(status_code=404, detail=f"Not found!, Error: {str(e)}")
    return employees

# 4
@employees_router.get("/employees/age-or-seniority")
def get_employees_age_or_seniority(database = Depends(get_database)):
    employees = DalManager.get_employees_by_age_or_seniority(database)
    if not employees:
        raise HTTPException(status_code=404, detail=f"Not found!, Error: {str(e)}")
    return employees

# 5
@employees_router.get("/employees/managers/excluding-departments")
def get_employees_manager_excluding_departments(database = Depends(get_database)):
    employees = DalManager.get_managers_excluding_departments(database)
    if not employees:
        raise HTTPException(status_code=404, detail=f"Not found!, Error: {str(e)}")
    return employees

# 6
@employees_router.get("/employees/by-lastname-and-age")
def get_employees_lastname_and_age(database = Depends(get_database)):
    employees = DalManager.get_employees_by_lastname_and_age(database)
    if not employees:
        raise HTTPException(status_code=404, detail=f"Not found!, Error: {str(e)}")
    return employees