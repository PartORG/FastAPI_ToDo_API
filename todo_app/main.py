from fastapi import FastAPI
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users


app = FastAPI()

# will create everything from models.py file and database.py file.
Base.metadata.create_all(bind=engine)


# health check route
@app.get("/healthy")
async def health_check():
    return {'status': 'Healthy'}


# add an auth router
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
