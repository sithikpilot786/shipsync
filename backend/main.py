from fastapi import FastAPI

app = FastAPI(
    title="ShipShync API",
    description="AI-Powered Dynamic Vehicle Routing & Delivery Optimization System",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "project": "ShipShync",
        "message": "Backend is running successfully 🚀",
        "version": "1.0.0",
        "status": "Healthy"
    }