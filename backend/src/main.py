from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Nginx handles the public face, but we keep CORS open for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

main_router = APIRouter(prefix="/api")

@main_router.get("/status")
def get_status():
    return {"status": "running", "environment": "poetry"}

app.include_router(main_router)