# 🔐 CipherVault - Secure Password Manager

This is my **Week 1 Project** for the AI/ML Fellowship! 
I built a local Password Manager called **CipherVault**. It takes a username and password, encrypts the password using Base64, and saves it securely to a CSV file.

I tried to use everything I learned this week: **OOP, File Handling, Modular Programming, and Streamlit.**

---

## 🧠 Concepts I Used (Briefly Explained)

Here is a breakdown of the logic behind my code:

### 1. Object-Oriented Programming (OOP)
Instead of writing messy functions everywhere, I used **Classes** to organize my data:
* **`class Secret`**: This is like a blueprint. It just holds the data for one single secret (Service, Username, Password).
* **`class CipherVault`**: This is the "Manager" class. It handles all the heavy lifting saving to files, reading from files, and encryption.

### 2. Modular Programming
I didn't want one huge file, so I split my code into three parts:
* **`utils.py`**: Holds the encryption logic (so it's reusable).
* **`manager.py`**: Holds the Classes and File handling logic.
* **`app.py`**: Holds *only* the Streamlit UI code.
* This makes the code clean and easier to debug!

### 3. File Handling (CSV)
I used Python's built-in `csv` library to store data so it doesn't disappear when I close the app.
* **`w` (Write Mode):** Used to create the file with headers if it doesn't exist.
* **`a` (Append Mode):** Used to add new passwords to the end of the file without deleting old ones.
* **`r` (Read Mode):** Used to pull data back into the app to show the table.

### 4. Encryption (Base64)
I didn't want passwords saved as plain text (that's unsafe!).
* I used the **`base64`** library to "encode" the passwords before saving them.
* When you view them in the app, the code "decodes" them back so you can read them.

### 5. Error Handling (`try...except`)
Files can be tricky. If the file is missing or corrupted, the app shouldn't crash.
* I wrapped my file operations in `try...except` blocks. If something goes wrong (like a Permission Error), the app catches it and prints a safe error message instead of crashing.

### 6. Streamlit UI
I used **Streamlit** to make it interactive:
* **`st.sidebar`**: To keep the "Add Secret" form separate from the main view.
* **`st.dataframe`**: To show the data in a neat table.
* **`st.checkbox`**: A cool toggle to Hide/Show passwords (privacy feature!).

---

## 🛠 How to Run It

1.  **Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

---
