from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.customers import router as customers_router

# Configure OpenAPI tags to improve generated docs grouping
openapi_tags = [
    {
        "name": "Customers",
        "description": "Operations related to managing customers (CRUD).",
    },
]

app = FastAPI(
    title="Customer Management API",
    description=(
        "FastAPI backend providing CRUD operations for managing customers.\n\n"
        "CORS: The server is configured to allow requests from '*' and http://localhost:3000 to "
        "support the React development server. Adjust allow_origins for production."
    ),
    version="0.1.0",
    openapi_tags=openapi_tags,
)

# Allow all origins for simplicity; restrict as needed (e.g., ["http://localhost:3000"])
# Note: If you tighten CORS to specific origins, keep allow_credentials aligned with browser needs.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    """
    Simple health check endpoint.

    Returns:
        JSON with a 'message' field indicating service health.
    """
    return {"message": "Healthy"}


# Mount API routers
app.include_router(customers_router, prefix="/api")
