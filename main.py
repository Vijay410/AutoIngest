
from fastapi import FastAPI
import uvicorn
from apis.endpoints.student_performance import router as student_performance_router



app = FastAPI(root_path="/api",
              openapi_url="/v1/openapi.json",
              docs_url="/v1/docs",
              title="Student Service",
              description="Student Service",
              )

app.include_router(student_performance_router, tags=["student_performance_router"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Service API"}

@app.get("/favicon.ico")
def favicon():
    return {}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True,
)