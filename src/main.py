from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Message": "This page is under developement"}
