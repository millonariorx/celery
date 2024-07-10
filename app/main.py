from fastapi import FastAPI
from app.tasks.celery_tasks import add, multiply, subtract, divide

app = FastAPI()

@app.get("/add/{a}/{b}")
def handle_add(a: int, b: int):
    result = add.delay(a, b)
    return {"task_id": result.id}

@app.get("/multiply/{a}/{b}")
def handle_multiply(a: int, b: int):
    result = multiply.delay(a, b)
    return {"task_id": result.id}

@app.get("/subtract/{a}/{b}")
def handle_subtract(a: int, b: int):
    result = subtract.delay(a, b)
    return {"task_id": result.id}

@app.get("/divide/{a}/{b}")
def handle_divide(a: int, b: int):
    result = divide.delay(a, b)
    return {"task_id": result.id}

@app.get("/run-multiple-tasks")
def run_multiple_tasks():
    task1 = add.delay(10, 5)
    task2 = multiply.delay(10, 5)
    task3 = subtract.delay(10, 5)
    task4 = divide.delay(10, 2)
    return {
        "task1_id": task1.id,
        "task2_id": task2.id,
        "task3_id": task3.id,
        "task4_id": task4.id
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
