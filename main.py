from fastapi import FastAPI
import uvicorn
from controllers.pdf_controller import router as pdf_router

app = FastAPI()

@app.get("/")
def read_root():
    return { "Hello": "world"}

app.include_router(pdf_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host = "127.0.0.1", port=8000, reload=True)
    
