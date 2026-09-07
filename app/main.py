from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Employee API is running"}


@app.get("/employees")
def get_employees():
    return [
        {"id": 1, "name": "John", "department": "IT"},
        {"id": 2, "name": "Alice", "department": "HR"},
        {"id": 3, "name": "David", "department": "Finance"},
    ]