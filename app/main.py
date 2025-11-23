from fastapi import FastAPI, HTTPException
from models import User

app = FastAPI()

fake_db = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"}
}

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
