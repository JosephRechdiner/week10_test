from fastapi import APIRouter, Depends, Request, HTTPException

employees_router = APIRouter()

def get_db(request: Request):
    return request.app.state.database