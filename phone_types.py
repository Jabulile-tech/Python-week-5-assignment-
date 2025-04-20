from phone_base import Cellphone

class Smartphone(Cellphone):
    def __init__(self, brand, model, screen_size, battery_capacity, os_type, storage):
        # Call parent class constructor
        super().__init__(brand, model, screen_size, battery_capacity)
        
        # Additional attributes specific to smartphones
        self._os_type = os_type
        self._storage = storage  # in GB
        self._installed_apps = []

    def install_app(self, app_name):
        if self._is_powered_on:
            self._installed_apps.append(app_name)
            return f"{app_name} has been installed"
        return "Please power on the device to install apps"

    def list_apps(self):
        return self._installed_apps

    def __str__(self):
        return f"{super().__str__()} - {self._os_type} - {self._storage}GB"


class FlipPhone(Cellphone):
    def __init__(self, brand, model, screen_size, battery_capacity, keyboard_type):
        super().__init__(brand, model, screen_size, battery_capacity)
        self._keyboard_type = keyboard_type
        self._is_flipped_open = False

    def flip_open(self):
        if not self._is_flipped_open:
            self._is_flipped_open = True
            return "Phone flipped open"
        return "Phone is already open"

    def flip_close(self):
        if self._is_flipped_open:
            self._is_flipped_open = False
            return "Phone flipped closed"
        return "Phone is already closed"

    def __str__(self):
        return f"{super().__str__()} - {self._keyboard_type} keyboard"
