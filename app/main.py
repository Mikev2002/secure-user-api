from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Secure User API is running"}
