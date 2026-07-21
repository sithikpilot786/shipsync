from fastapi import FastAPI
from backend.routes.vehicles import router as vehicle_router

app = FastAPI(
    title="ShipSync API",
    description="AI-Powered Dynamic Vehicle Routing & Delivery Optimization System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "project": "ShipSync",
        "message": "Backend is running successfully 🚀",
        "version": "1.0.0",
        "status": "Healthy"
    }


app.include_router(vehicle_router)