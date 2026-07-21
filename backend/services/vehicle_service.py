from backend.models.vehicle import Vehicle


class VehicleService:
    def __init__(self):
        self.vehicles = [
            Vehicle(
                vehicle_id=1,
                driver_name="Rahul",
                vehicle_type="Mini Truck",
                capacity=1000,
                status="Available",
                latitude=10.7905,
                longitude=78.7047,
            ),
            Vehicle(
                vehicle_id=2,
                driver_name="Arun",
                vehicle_type="Van",
                capacity=750,
                status="Delivering",
                latitude=10.8030,
                longitude=78.6890,
            ),
        ]

    def get_all_vehicles(self):
        return self.vehicles