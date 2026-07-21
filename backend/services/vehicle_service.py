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

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        return vehicle

    def get_vehicle_by_id(self, vehicle_id: int):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    def update_vehicle(self, vehicle_id: int, updated_vehicle: Vehicle):
        for index, vehicle in enumerate(self.vehicles):
            if vehicle.vehicle_id == vehicle_id:
                self.vehicles[index] = updated_vehicle
                return updated_vehicle
        return None

    def delete_vehicle(self, vehicle_id: int):
        for index, vehicle in enumerate(self.vehicles):
            if vehicle.vehicle_id == vehicle_id:
                deleted_vehicle = self.vehicles.pop(index)
                return deleted_vehicle
        return None