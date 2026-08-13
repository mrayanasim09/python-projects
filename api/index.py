from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import os

app = FastAPI(title="Python Projects API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
async def root():
    return {"message": "Python Projects — API", "routes": ["/api/projects"]}


@app.get("/api/projects")
async def projects():
    base = os.path.dirname(os.path.dirname(__file__))
    items = []
    for name in sorted(os.listdir(base)):
        if name.startswith('.') or name in ('__pycache__', '.git', 'api', '.venv', '.venv3'):
            continue
        path = os.path.join(base, name)
        if os.path.isdir(path):
            items.append({"name": name, "type": "directory"})
        elif os.path.isfile(path) and name.endswith('.py'):
            items.append({"name": name, "type": "file"})
    return {"projects": items}


# Required for Vercel serverless — wraps ASGI app as AWS Lambda handler
handler = Mangum(app)
