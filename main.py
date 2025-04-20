from phone_types import Smartphone, FlipPhone

def main():
    # Create instances of different phone types
    iphone = Smartphone("Apple", "iPhone 13", 6.1, 3240, "iOS", 128)
    samsung_flip = FlipPhone("Samsung", "Galaxy Flip", 6.7, 3300, "Touch")

    # Test smartphone features
    print(iphone.power_on())
    print(iphone.install_app("Instagram"))
    print(iphone.install_app("WhatsApp"))
    print(f"Installed apps: {iphone.list_apps()}")
    print(iphone.charge_battery(1000))
    print(iphone)

    # Test flip phone features
    print("\n" + "="*50 + "\n")
    print(samsung_flip.power_on())
    print(samsung_flip.flip_open())
    print(samsung_flip.get_battery_level())
    print(samsung_flip)

if __name__ == "__main__":
    main()
