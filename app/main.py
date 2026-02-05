from fastapi import FastAPI
from contextlib import asynccontextmanager
from connection import MongoManager
from routes import employees_router

file_path = './data/employee_data_advanced.json'

@asynccontextmanager
async def lifespan(app :FastAPI):
    app.state.manager = MongoManager()
    app.state.client = app.state.manager.get_client()
    app.state.database = app.state.client["database"]
    app.state.manager.seed_data(file_path, app.state.database)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(employees_router)