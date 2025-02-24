from fastapi import FastAPI
import uvicorn
from controllers.pdf_controller import router as pdf_router

app = FastAPI()

@app.get("/")
def read_root():
    return { "Hello": "world on render"}

app.include_router(pdf_router)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)  
    
