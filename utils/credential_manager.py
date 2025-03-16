import keyring
import getpass


def set_credentials(service):
    """
    Prompt the user to enter and securely store credentials in the system keyring.
    """
    username = input(f"Enter your {service} username: ")
    password = input(f"Enter your {service} password: ")

    keyring.set_password(service, "username", username)
    keyring.set_password(service, "password", password)
    print(f"Credentials for {service} saved successfully!")


def get_credentials(service):
    """
    Retrieve stored credentials from the system keyring.
    """
    username = keyring.get_password(service, "username")
    password = keyring.get_password(service, "password")

    if username and password:
        return username, password
    else:
        raise ValueError(f"No credentials found for {service}. Please set them first.")


if __name__ == "__main__":
    service_name = "GitHub"
    set_credentials(service_name)
