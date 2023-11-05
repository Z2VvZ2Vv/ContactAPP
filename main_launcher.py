#  _____                _                 _              _____   _____
# / ____|              | |               | |      /\    |  __ \ |  __ \
#| |       ___   _ __  | |_   __ _   ___ | |_    /  \   | |__) || |__) |
#| |      / _ \ | '_ \ | __| / _` | / __|| __|  / /\ \  |  ___/ |  ___/
#| |____ | (_) || | | || |_ | (_| || (__ | |_  / ____ \ | |     | |
# \_____| \___/ |_| |_| \__| \__,_| \___| \__|/_/    \_\|_|     |_|
#
# v1 by Geoffrey
# This script is the main launcher file of the ContactAPP.

from console import *
from cryptography.fernet import Fernet
import readline

def generate_key():
    """
    Generates a key using the Fernet algorithm and returns it as a string.

    Returns:
        str: The generated key as a string.
    """
    key = Fernet.generate_key()[:44]
    key_str = str(key)[2:-1]
    return key_str

def check_first_run():
    """
    Check if it is the first run of the program.

    Returns:
        bool: True if it is the first run, False otherwise.
    """
    if os.path.exists("data.enc") == True:
        with open("data.enc", "r") as file:
            data = file.read()
            if data == "":
                return True
    elif os.path.exists("data.enc") == False:
        open("data.enc","w").close
        return True
    else:
        return False

def encrypt_file(key):
    """
    Encrypts a file using the provided key.

    Parameters:
        key (bytes): The encryption key used to encrypt the file.

    Returns:
        None
    """
    fernet = Fernet(key)
    with open("temp_data.txt", "rb") as file1:
        data = file1.read()
    encrypted_data = fernet.encrypt(data)
    with open("data.enc", "wb") as file2:
        file2.write(encrypted_data)

def decrypt_file(key):
    """
    Decrypts a file using the provided key.

    Parameters:
        key (bytes): The key used for decryption.

    Returns:
        None
    """
    fernet = Fernet(key)
    with open("data.enc", "rb") as file1:
        encrypted_data = file1.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open("temp_data.txt", "wb") as file2:
        file2.write(decrypted_data)
    open("contactapp_encrypted_run","w").close

def check_if_encryted():
    """
    Check if the file "data.enc" is encrypted.

    This function reads the content of the file "data.enc" and checks if the string "|" is present in the content. If the string is present, it returns False. If the content of the file is empty, it also returns False. Otherwise, it returns True.

    Returns:
        bool: True if the file is not encrypted, False otherwise.
    """
    with open("data.enc", "r") as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if "|" in content :
            return False
        elif content == "":
            return False
        else:
            return True

def check_if_crash_not_encrypted():
    """
    Check if the ContactAPP application crashed and was not encrypted.

    Returns:
        bool: True if the ContactAPP application was interrupted unexpectedly and not encrypted, False otherwise.
    """
    if os.path.exists("contactapp_was_running") == True:
        logo()
        print("[!] Your ContactAPP application was interrupted unexpectedly!")
        print("--------------------------------------------------------")
        print("Please be careful, and close the app properly from main menu!")
        print()
        input("Press ENTER to continue")
        return True
    else:
        with open("data.enc", "r") as file1:
            data = file1.read()
        with open("temp_data.txt", "w") as file2:
            file2.write(data)
        return False

def check_if_crash_encrypted():
    """
    Check if the encrypted contact app has crashed.

    Returns:
        bool: True if the encrypted contact app has crashed, False otherwise.
    """
    if os.path.exists("contactapp_encrypted_run") == True:
        return True
    else:
        with open("data.enc","r+") as file:
            data = file.read()
            print(data)
            if data == "":
                file.write("first_lauch_app_encrypted")
            file.close()
        return False

def ending_app(key):
    """
    Ends the application by encrypting a file and removing temporary files.

    Parameters:
        key (any): The encryption key used to encrypt the file. If None, the function will encrypt a file named "temp_data.txt" and remove it afterwards.

    Returns:
        None: This function does not return anything.
    """
    if key != None:
        encrypt_file(key)
        os.remove("temp_data.txt")
        os.remove("contactapp_encrypted_run")
        return None
    else:
        with open("temp_data.txt", "r") as file1:
            data = file1.read()
        with open("data.enc", "w") as file2:
            file2.write(data)
        os.remove("temp_data.txt")
        os.remove("contactapp_was_running")
        return None


def mainlauncher():
    """
    This function is the main launcher of the ContactAPP application. It performs the following steps:
    1. Calls the `logo()` function to display the ContactAPP logo.
    2. Checks if it is the first run of the application by calling the `check_first_run()` function.
        - If it is the first run, it prompts the user to encrypt their contacts.
        - If the user chooses to encrypt their contacts, it generates a secret key by calling the `generate_key()` function.
        - It checks if the application crashed during encryption by calling the `check_if_crash_encrypted()` function.
        - It opens the `contactapp_encrypted_run` file to indicate that the application has been encrypted.
        - It calls the `main()` function to start the application.
        - It calls the `ending_app()` function with the secret key as an argument.

    3. Checks if the application crashed during encryption by calling the `check_if_crash_encrypted()` function.
        - It generates a new secret key by calling the `generate_key()` function.
        - It calls the `main()` function to start the application.
        - It calls the `ending_app()` function with the new secret key as an argument.
        
    4. Checks if the contacts are encrypted by calling the `check_if_encrypted()` function.
        - If the contacts are encrypted, it displays a message and asks the user to provide the secret key.
        - It attempts to decrypt the file using the provided secret key by calling the `decrypt_file()` function.
        - It catches any exceptions and prompts the user to enter the correct secret key.
        - It displays a message if the user enters the wrong secret key too many times.
    """
    logo()
    if check_first_run() == True:
        print("Welcome for your first startup of ContactAPP !")
        print("--------------------------------------------------------")
        if input("Do you want to encrypt your contacts ? (y/N) : ") == "y":
            key = generate_key()
            print(f"""There it is ! Your secret key '{key}', conserve it ! In case you change your mind, please delete the file 'data.enc'.""")
            print()
            input("Press ENTER to continue")
            check_if_crash_encrypted()
            open("contactapp_encrypted_run","w").close
            main()
            ending_app(key)
            return None
        else:
            print("Data not encrypted. In case you change your mind, please delete the file 'data.enc'.")
            print()
            input("Press ENTER to continue")
            main()
            ending_app(None)
            return None
        
    elif check_if_crash_encrypted() == True:
        logo()
        print("[!] Your ContactAPP application was interrupted unexpectedly!")
        print("Due to security reasons, ContactAPP can't encrypt the contacts with your old secret key !")
        print("--------------------------------------------------------")
        key = generate_key()
        print(f"""There is your new secret key '{key}', conserve it ! In case you change your mind, please delete the file 'data.enc'.""")
        print()
        input("Read carefully and then press ENTER to continue.")
        main()
        ending_app(key)
        return None
    
    elif check_if_encryted() == True:
        logo()
        print("Welcome, ContactAPP requires the secret key to decrypt contacts !")
        print("--------------------------------------------------------")
        for i in range(3):
            try:
                key = input("Your secret key : ")
                decrypt_file(key)
            except:
                print("Wrong secret key !")
                print()
                pass
                print("Fail, too many attempts !")
                return None
            main()
            ending_app(key)
            return None
    
    else:
        check_if_crash_not_encrypted()
        main()
        ending_app(None)
        return None
    

if __name__=="__main__":
    mainlauncher()