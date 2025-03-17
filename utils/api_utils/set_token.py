import sys

try:
    import win32cred  # Windows Credential Manager
except ImportError:
    win32cred = None  # Handle missing module on macOS/Linux

import keyring  # macOS/Linux Keychain


def store_token(token):
    """Stores the GitHub token securely based on the operating system."""
    service_name = "GitHub_Automation"
    account_name = "GitHub_Token"

    if sys.platform == "win32":
        if not win32cred:
            raise ImportError("win32cred module not found. Install with `pip install pywin32`")

        credential = {
            "Type": win32cred.CRED_TYPE_GENERIC,
            "TargetName": service_name,
            "UserName": account_name,
            "CredentialBlob": token,
            "Persist": win32cred.CRED_PERSIST_LOCAL_MACHINE
        }
        win32cred.CredWrite(credential, 0)

    else:  # macOS & Linux
        keyring.set_password(service_name, account_name, token)

    print("✅ GitHub token stored successfully!")


def retrieve_token():
    """Retrieves the stored GitHub token securely."""
    service_name = "GitHub_Automation"
    account_name = "GitHub_Token"

    if sys.platform == "win32":
        if not win32cred:
            raise ImportError("win32cred module not found. Install with `pip install pywin32`")

        credentials = win32cred.CredRead(service_name, win32cred.CRED_TYPE_GENERIC, 0)
        if credentials:
            # Handle UTF-16 encoded string (strip null bytes)
            raw_blob = credentials["CredentialBlob"]
            if isinstance(raw_blob, str):
                return raw_blob
            elif isinstance(raw_blob, bytes):
                # Try decoding as UTF-16 and removing null bytes
                if b'\x00' in raw_blob:
                    # This is likely UTF-16 encoded
                    return raw_blob.decode('utf-16-le')
                else:
                    # Regular UTF-8
                    return raw_blob.decode('utf-8')

    else:  # macOS & Linux
        return keyring.get_password(service_name, account_name)

    return None  # If token is not found


if __name__ == "__main__":
    token_input = input("Enter your GitHub Token: ").strip()
    store_token(token_input)