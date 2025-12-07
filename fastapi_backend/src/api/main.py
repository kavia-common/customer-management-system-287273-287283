from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.customers import router as customers_router

app = FastAPI(
    title="Customer Management API",
    description="FastAPI backend providing CRUD operations for managing customers.",
    version="0.1.0",
)

# Allow all origins for simplicity; restrict as needed (e.g., ["http://localhost:3000"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    """Simple health check endpoint."""
    return {"message": "Healthy"}


# Mount API routers
app.include_router(customers_router, prefix="/api")
