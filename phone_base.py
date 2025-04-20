class Cellphone:
    def __init__(self, brand, model, screen_size, battery_capacity):
        # Private attributes (encapsulation)
        self._brand = brand
        self._model = model
        self._screen_size = screen_size  # in inches
        self._battery_capacity = battery_capacity  # in mAh
        self._is_powered_on = False
        self._current_battery = battery_capacity

    # Getter methods (encapsulation)
    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_battery_level(self):
        return (self._current_battery / self._battery_capacity) * 100

    # Methods
    def power_on(self):
        if not self._is_powered_on:
            self._is_powered_on = True
            return f"{self._brand} {self._model} is powering on..."
        return "Device is already on"

    def power_off(self):
        if self._is_powered_on:
            self._is_powered_on = False
            return f"{self._brand} {self._model} is shutting down..."
        return "Device is already off"

    def charge_battery(self, amount):
        if self._current_battery + amount <= self._battery_capacity:
            self._current_battery += amount
        else:
            self._current_battery = self._battery_capacity
        return f"Battery level: {self.get_battery_level()}%"

    def __str__(self):
        return f"{self._brand} {self._model} - {self._screen_size} inch display"
