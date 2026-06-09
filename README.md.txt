# 🐉 Dragon Password (v1.1)
**Developed by:** [yogender-cyber](https://github.com)

Dragon Password ek advanced, open-source aur high-security local password manager tool hai. Isko is tarah se design kiya gaya hai ki ise ek normal insaan bhi aasani se use kar sake aur professional hackers/security researchers iske encryption standards par bharosa kar sakein.

---

## ⚡ Power of Dragon Password (Tool Features)
*   **Zero-Knowledge System:** Aapka master password kahin bhi plain text me save nahi hota. Aapke alawa aapka data koi nahi dekh sakta, yahan tak ki developer bhi nahi.
*   **AES-256 Bit Encryption:** Industry-standard encryption jo aapke saare saved passwords ko ek encrypted database file (`dragon_vault.db`) me local computer par lock rakhta hai. Is encryption ko brute-force karna namumkin hai.
*   **Memory Scavenging Protection:** Jaise hi aap encryption/decryption process poora karte hain, ye tool use RAM (memory) se overwrite karke delete kar deta hai taaki koi malware ise memory dump se chura na sake.
*   **Offline First (100% Safe):** Ye tool internet ka use nahi karta, isliye cloud hacking ya remote server leak ka koi khatra nahi hai.
*   **Auto Generator:** Ek click me strong aur unhackable random passwords generate karne ki power.

---

## 📖 User Help Guide: Is Tool Ko Kaise Use Karein? (यूज़र गाइड)

### 🚀 Step 1: Requirements & Installation
Is tool ko chalane ke liye aapke computer me Python install hona chahiye. Terminal ya Command Prompt (CMD) me ye commands chalayein:
```bash
pip install cryptography
python dragon_password.py
```

### 🔒 Step 2: Master Password Set Karna
1. Jab aap tool ko open karenge, sabse upar aapko ek **Master Password** set karna hoga (Jaise: `my_secret_key`).
2. *⚠️ Dhyan rahe:* Ye password aapko kabhi nahi bhoolna hai. Agar aap ye bhool gaye, toh aapka data hamesha ke liye lock ho jayega kyunki iska koi "Forgot Password" option nahi hota!

### ➕ Step 3: Websites Ka Data Save Karna
1. **Website Name** me jis site ka account hai wo likhein (Jaise: `Facebook` ya `Gmail`).
2. **Username/Email** me apna login ID dalein.
3. **Password to Hide** me apna password likhein, ya fir upar diye gaye **🎲 Auto Generate Password** button par click karke ek strong password bana lein.
4. **🔒 Save Encrypted into Vault** button par click karein. Aapka data instant lock hokar secure database me chala jayega.

### 👁️ Step 4: Saved Passwords Ko Dekhna
1. Jab bhi aapko apne passwords dekhne hon, upar apna sahi **Master Password** enter karein.
2. Sabse niche diye gaye **👁️ View My Saved Passwords** button par click karein.
3. Ek nayi window khulegi jahan aapko aapke saare saved accounts ki list (Website, Username, aur Decrypted Password) saaf-saaf dikhai degi.

---
*Developed with ❤️ for the Cyber Security Community by yogender-cyber.*
