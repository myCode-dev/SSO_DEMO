### **NCU PORTAL OAuth 2.0 Integration Example**

This example demonstrates how to integrate **NCU PORTAL's OAuth 2.0 authorization mechanism** into a Python Flask application to retrieve user information.

---

## **🛠 Technologies Used**
- **Backend Framework:** Python Flask

---

## **📖 Integration Documentation**
Official documentation: [NCU Portal OAuth Docs](https://github.com/ncucc/portal4g-doc)

---

## **🚀 Setup & Instructions**

### **1️⃣ Clone the Project**
First, clone the project to your local machine. Open the terminal and run:

```bash
git clone https://github.com/Celia-code/SSO_DEMO.git
```

Navigate into the project directory:

```bash
cd project
```

---

### **2️⃣ Set Environment Variables**
This project uses a `.env` file to configure environment variables.  
First, copy the example environment file and rename it to `.env`:

#### **Windows:**
```bash
copy example.env .env
```

#### **Linux/Mac:**
```bash
cp example.env .env
```

Then, open the `.env` file and modify the following variables:

| Variable           | Description                                       |
|--------------------|---------------------------------------------------|
| `CLIENT_ID`       | Client ID provided by NCU Portal                   |
| `CLIENT_SECRET`   | Client Secret provided by NCU Portal               |
| `CALLBACK_URL`    | Redirect URL for the application                   |
| `AUTHORIZATION_URL` | OAuth 2.0 authorization endpoint (`https://portal.ncu.edu.tw/oauth2/authorization`) |
| `TOKEN_URL`       | OAuth 2.0 token retrieval endpoint (`https://portal.ncu.edu.tw/oauth2/token`) |
| `USER_INFO_URL`   | User information retrieval endpoint (`https://portal.ncu.edu.tw/apis/oauth/v1/info`) |

---

### **3️⃣ Install Dependencies**
Install the required dependencies using:

```bash
pip install -r requirements.txt
```

---

### **4️⃣ Run the Project**
Start the Flask application with:

```bash
python main.py
```

---
