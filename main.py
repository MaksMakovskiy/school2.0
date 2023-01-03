import uvicorn  # pip install uvicorn
from fastapi import FastAPI, Request, Form  # pip install fastapi
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from model import UserData, UsersInfo
import uuid
from random import randint

app = FastAPI()

templates = Jinja2Templates(directory="templates")


users_s = []
for _ in range(8):
    users_s.append(UserData(name=f"{uuid.uuid4()}", age=randint(1, 15)))
print(users_s)

users = UsersInfo(all_users=users_s)


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        "base.html.jinja", {"request": request, "users": users}
    )


@app.get("/add_user", response_class=HTMLResponse)
def add_user(request: Request):
    return templates.TemplateResponse(
        "new_user.html.jinja", {"request": request, "users": users}
    )


@app.post("/new_user", response_class=RedirectResponse, status_code=303)
def new_user(name: str = Form(...), age: int = Form(...)):
    users.add_user(name, age)
    return "/"


if __name__ == "__main__":
    uvicorn.run(app)
