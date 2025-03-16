from configparser import ConfigParser
import os

# Get the absolute path of object.ini
config_path = os.path.join(os.path.dirname(__file__), "../config/object.ini")

# Load object.ini
config = ConfigParser()
config.read(config_path)


def get_object(variable):
    """ Fetch XPath value from object.ini """

    # Debugging: Print all sections and keys
    print(f"Loaded sections: {config.sections()}")
    for section in config.sections():
        print(f"Keys in [{section}]: {dict(config.items(section))}")

    for section in config.sections():
        if config.has_option(section, variable):
            return config.get(section, variable)

    raise ValueError(f"Error: Element '{variable}' not found in object.ini.")
