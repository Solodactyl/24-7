import os
import random
import string
import time

def display_banner():
    print(r"""

███████╗ ██████╗ ██╗      ██████╗     ██████╗ ██╗      █████╗ ██╗   ██╗███████╗
██╔════╝██╔═══██╗██║     ██╔═══██╗    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝╚══███╔╝
███████╗██║   ██║██║     ██║   ██║    ██████╔╝██║     ███████║ ╚████╔╝   ███╔╝ 
╚════██║██║   ██║██║     ██║   ██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝   ███╔╝  
███████║╚██████╔╝███████╗╚██████╔╝    ██║     ███████╗██║  ██║   ██║   ███████╗
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════
                                                       
                              Solo Playz
    """)

def generate_random_string(length=100):
    """Generate a random string of letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_edit_delete_file():
    """Create, edit, and delete a random file repeatedly in a specified folder."""
    folder_name = "DONT DELETE THIS FOLDER"
    os.makedirs(folder_name, exist_ok=True)  # Ensure the folder exists

    while True:
        try:
            # Generate a random file name
            file_name = os.path.join(folder_name, f"{generate_random_string(8)}.txt")

            # Create a file with random content
            with open(file_name, "w") as file:
                for _ in range(random.randint(10, 100)):
                    file.write(generate_random_string(100) + "\n")
            print(f"Created: {file_name}")

            time.sleep(2)

            # Edit the file with new random content
            with open(file_name, "w") as file:
                for _ in range(random.randint(10, 100)):
                    file.write(generate_random_string(100) + "\n")
            print(f"Edited: {file_name}")

            time.sleep(1)

            # Delete the file
            os.remove(file_name)
            print(f"Deleted: {file_name}")

            time.sleep(1)

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)

if __name__ == "__main__":
    display_banner()
    create_edit_delete_file()
