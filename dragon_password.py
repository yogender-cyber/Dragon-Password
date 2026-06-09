import os
import json
import base64
import random
import string
from tkinter import *
from tkinter import messagebox, ttk
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Tool Name: Dragon Password 🐉
# Developer: yogender-cyber 👨‍💻

VAULT_FILE = "dragon_vault.db"
SALT = b'dragon_secure_salt_yogender' # Security Salt

def derive_key(master_password):
    """Master password se security key generate karne ke liye"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

def encrypt_data(key, plain_text):
    """AES Encryption mechanism"""
    from cryptography.fernet import Fernet
    f = Fernet(key)
    return f.encrypt(plain_text.encode()).decode()

def decrypt_data(key, encrypted_text):
    """AES Decryption mechanism"""
    from cryptography.fernet import Fernet
    try:
        f = Fernet(key)
        return f.decrypt(encrypted_text.encode()).decode()
    except Exception:
        return None

def generate_strong_password():
    """Automatic Strong Password Generator"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    # 14 characters ka strong password
    strong_pass = "".join(random.choice(characters) for i in range(14))
    entry_pass.delete(0, END)
    entry_pass.insert(0, strong_pass)

def save_credentials():
    """Data ko local vault me secure save karne ke liye"""
    master_pass = entry_master.get()
    website = entry_web.get().strip()
    username = entry_user.get().strip()
    password = entry_pass.get().strip()
    
    if not master_pass or not website or not username or not password:
        messagebox.showerror("Error", "Saari fields bharna jaruri hai!")
        return
        
    key = derive_key(master_pass)
    encrypted_password = encrypt_data(key, password)
    
    data = {}
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
                
    data[website] = {"username": username, "password": encrypted_password}
    
    with open(VAULT_FILE, 'w') as f:
        json.dump(data, f, indent=4)
        
    messagebox.showinfo("Success", f"🐉 Dragon Password: {website} ka data secure lock ho gaya!")
    
    # RAM Security: Data clear karna
    entry_web.delete(0, END)
    entry_user.delete(0, END)
    entry_pass.delete(0, END)

def view_vault():
    """Saved passwords ko decrypt karke dekhne ke liye new window"""
    master_pass = entry_master.get()
    if not master_pass:
        messagebox.showerror("Error", "Pehle apna Master Password upar enter karein!")
        return
        
    if not os.path.exists(VAULT_FILE):
        messagebox.showinfo("Vault Empty", "Abhi tak koi password save nahi kiya gaya hai.")
        return

    key = derive_key(master_pass)
    
    with open(VAULT_FILE, 'r') as f:
        data = json.load(f)
        
    # New GUI Window for Vault
    vault_window = Toplevel(root)
    vault_window.title("Dragon Vault Content")
    vault_window.geometry("500x300")
    vault_window.configure(bg="#121212")
    
    Label(vault_window, text="🔒 APKE SECURE PASSWORDS 🔒", fg="#00FF00", bg="#121212", font=("Courier", 12, "bold")).pack(pady=10)
    
    # Text Box to show data
    txt_area = Text(vault_window, bg="#1a1a1a", fg="white", font=("Arial", 10))
    txt_area.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    success = False
    for website, info in data.items():
        decrypted_pass = decrypt_data(key, info["password"])
        if decrypted_pass is None:
            messagebox.showerror("Wrong Key", "Master Password galat hai! Data decrypt nahi ho saka.")
            vault_window.destroy()
            return
        
        success = True
        txt_area.insert(END, f"🌐 Website: {website}\n👤 Username: {info['username']}\n🔑 Password: {decrypted_pass}\n-------------------------\n")
    
    txt_area.config(state=DISABLED) # Read only layout

# ---- Main GUI Screen ----
root = Tk()
root.title("Dragon Password v1.1 - by yogender-cyber")
root.geometry("450x480")
root.configure(bg="#121212")

lbl_title = Label(root, text="🐉 DRAGON PASSWORD 🐉", fg="#00FF00", bg="#121212", font=("Courier", 16, "bold"))
lbl_title.pack(pady=10)

lbl_dev = Label(root, text="Developed by: yogender-cyber", fg="#888888", bg="#121212", font=("Arial", 10, "italic"))
lbl_dev.pack()

# Input UI Fields
Label(root, text="Master Password (Main Lock):", fg="white", bg="#121212").pack(pady=5)
entry_master = Entry(root, show="*", width=30, bg="#222222", fg="white", insertbackground="white")
entry_master.pack()

Label(root, text="Website Name (e.g. Google):", fg="white", bg="#121212").pack(pady=5)
entry_web = Entry(root, width=30, bg="#222222", fg="white", insertbackground="white")
entry_web.pack()

Label(root, text="Username / Email:", fg="white", bg="#121212").pack(pady=5)
entry_user = Entry(root, width=30, bg="#222222", fg="white", insertbackground="white")
entry_user.pack()

Label(root, text="Password to Hide:", fg="white", bg="#121212").pack(pady=5)
entry_pass = Entry(root, width=30, bg="#222222", fg="white", insertbackground="white")
entry_pass.pack()

# Buttons Layout
btn_gen = Button(root, text="🎲 Auto Generate Password", bg="#333333", fg="#00FF00", font=("Arial", 9, "bold"), command=generate_strong_password)
btn_gen.pack(pady=5)

btn_save = Button(root, text="🔒 Save Encrypted into Vault", bg="#00FF00", fg="black", font=("Arial", 10, "bold"), command=save_credentials)
btn_save.pack(pady=15)

btn_view = Button(root, text="👁️ View My Saved Passwords", bg="#0088FF", fg="white", font=("Arial", 10, "bold"), command=view_vault)
btn_view.pack(pady=5)

root.mainloop()
