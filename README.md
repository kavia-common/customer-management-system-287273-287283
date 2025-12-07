# customer-management-system-287273-287283

This project contains:
- fastapi_backend: FastAPI service exposing REST endpoints for managing customers.
- react_frontend: React UI (runs on port 3000) that communicates with the backend.

Backend (FastAPI)
- Base URL: http://localhost:3001
- OpenAPI Docs: http://localhost:3001/docs
- Health: GET http://localhost:3001/

CORS
- CORS is enabled to allow "*" and http://localhost:3000 to support local development with the React app.
- For production, restrict allow_origins in fastapi_backend/src/api/main.py.

Primary API Endpoints
- GET /api/customers
- POST /api/customers
- GET /api/customers/{customer_id}
- PUT /api/customers/{customer_id}
- DELETE /api/customers/{customer_id}

Frontend Integration
- The React app should use the environment variable REACT_APP_API_BASE to build requests to the backend.
- Example (in React):
  const API_BASE = process.env.REACT_APP_API_BASE || 'http://localhost:3001';
  fetch(`${API_BASE}/api/customers`)

Environment
- Copy .env.example to .env and adjust values as needed, especially REACT_APP_API_BASE.

Smoke Test Checklist (end-to-end)
1) Create -> List
   - POST /api/customers to create a customer.
   - GET /api/customers to verify the new customer appears.
2) Detail -> Edit -> Save
   - GET /api/customers/{id}
   - PUT /api/customers/{id} with updated fields
   - GET /api/customers/{id} to confirm updates
3) Delete
   - DELETE /api/customers/{id}
   - GET /api/customers to confirm removal

Notes
- The backend uses an in-memory store; data will reset when the server restarts.