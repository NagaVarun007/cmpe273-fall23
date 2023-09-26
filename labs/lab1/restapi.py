from fastapi import FastAPI

app = FastAPI(
"title": "Demo API",
"description": "Demo API with FastAPI",
"version": "0.1.0"
)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}




