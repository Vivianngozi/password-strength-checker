# 🔐 Password Strength Checker

A Python-based **Password Strength Checker** that evaluates the strength of passwords based on multiple security criteria.

---

## ⚙️ Core Functionality

The script checks the strength of a password based on several key factors:

- **🔢 Length:**  
  Ensures the password has a minimum length (**8+ characters**).

- **🔡 Uppercase & Lowercase Letters:**  
  Verifies the presence of both uppercase (**A-Z**) and lowercase (**a-z**) letters.

- **🔢 Numbers:**  
  Looks for at least one **numeric character** (**0-9**).

- **⚡ Special Characters:**  
  Ensures inclusion of special symbols (**!@#$%^&***, etc.).

- **🚫 Common Passwords Check:**  
  Compares against a list of **weak/common passwords** (e.g., `"123456"`, `"password"`) to prevent easily guessable passwords.

---

## 📊 Strength Evaluation Logic

The script assigns points based on the above checks and categorizes the password as:

- **🔴 Weak** — Fails most checks (e.g., short, lacks character diversity).  
- **🟡 Moderate** — Passes some checks but isn't strong enough.  
- **🟢 Strong** — Meets all requirements for a secure password.

---

## 👥 User Interaction

- Prompts the user to **input a password**.  
- Validates the input against all the criteria.  
- Provides real-time feedback like:  
  ```
  Your password is Weak. Try adding special characters.
  ```  
  or  
  ```
  Strong password! 💪
  ```

---

## 🚨 Error Handling

- **Empty Input:**  
  Handles cases where the user hits **enter** without typing a password.

- **Special Characters:**  
  Manages unexpected or special characters gracefully.

- **User-Friendly Errors:**  
  Provides clear error messages and guidance for creating stronger passwords.

---

## 🚀 How to Run the Script

### 💾 **1. Write the Script**
1. Open your code editor (**VS Code**, **PyCharm**, etc.).  
2. Paste the script into a new file named:  
   ```
   password_checker.py
   ```  

### 🖥️ **2. Execute the Script**
1. Open **Terminal** or **Command Prompt**.  
2. Navigate to the directory where the script is saved:  
   ```bash
   cd /path/to/your/script/
   ```  
3. Run the script:  
   ```bash
   python password_checker.py
   ```

### 🔍 **3. Test It Out**
1. When prompted, **enter different passwords** to see how the strength evaluation works.  
2. Review the feedback and adjust your password as needed.
