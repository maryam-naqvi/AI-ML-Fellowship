import csv
import os
from utils import encrypt_password, decrypt_password

class Secret:
    
    def __init__(self, service, username, password):
        self.service = service
        self.username = username
        self.password = password

class CipherVault:
    
    def __init__(self, filename="secrets.csv"):
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self):
        
        if not os.path.exists(self.filename):
            try:
                with open(self.filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Service", "Username", "Encrypted_Password"])
            except IOError as e:
                print(f"Error initializing vault: {e}")

    def add_secret(self, secret_obj):
        
        try:
            
            encrypted_pw = encrypt_password(secret_obj.password)
            
            # 2. Append to file
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([secret_obj.service, secret_obj.username, encrypted_pw])
            
            
            return True, "Secret saved securely!"
            
        except Exception as e:
            
            return False, f"Error saving secret: {e}"

    def get_all_secrets(self):
        
        secrets = []
        if os.path.exists(self.filename):
            try:
                with open(self.filename, mode='r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        try:
                            decrypted_pw = decrypt_password(row["Encrypted_Password"])
                            secrets.append({
                                "Service": row["Service"],
                                "Username": row["Username"],
                                "Password": decrypted_pw  
                            })
                        except:
                            continue 
            except Exception:
                pass
        return secrets