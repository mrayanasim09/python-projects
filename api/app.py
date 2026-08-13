from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Python Projects — minimal API", "routes": ["/projects"]}


@app.get("/projects")
async def projects():
    base = os.path.dirname(os.path.dirname(__file__))
    items = []
    for name in sorted(os.listdir(base)):
        if name.startswith('.') or name in ('__pycache__', '.git'):
            continue
        path = os.path.join(base, name)
        if os.path.isdir(path):
            items.append(name)
        elif os.path.isfile(path) and name.endswith('.py'):
            items.append(name)
    return {"projects": items}
