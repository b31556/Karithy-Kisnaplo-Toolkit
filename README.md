# Karithy Kisnapló Toolkit

**Author:** HOGOLYO

---

## ⚠️ Disclaimer

**Use only for research purposes.**  
This toolkit is intended strictly for **educational and research purposes**. By using this software, you agree that the author is **not responsible for any misuse**, data loss, or legal consequences. Ensure you comply with **all applicable laws and ethical guidelines** when using this toolkit. This project does **not endorse unauthorized access** to any private or sensitive data.

---

## 📌 What is this?

The **Karithy Kisnapló Toolkit** is a collection of tools designed to interact with the Kisnapló system for research, data analysis, and visualization purposes. It can extract and organize school-related data such as timetables and birthdays in a structured format (Excel, JSON, Sqlite) for easy analysis.

---

## 🗂 Table of Contents

- [📊 Charts: What You Need / Tool Use](#-charts-what-you-need--tool-use)
    
- [🛠 Tools](#-tools)
    
    - [All Timetables](#all-timetables)
        
    - [Birthday Scraper](#birthday-scraper)
    
-  [How to Get Your KSNPLSID](#how-to-get-your-ksnplsid)

---

## 📊 Charts: What You Need / Tool Use

| Tool                                        | What You Need           | Output                          | What it does                 |
| ------------------------------------------- | ----------------------- | ------------------------------- | ---------------------------- |
| [All Timetables](#all-timetables)           | Active Kisnapló account | Excel, JSON, Interactive Viewer | Gets all clases timetables   |
| [Birthday Scraper](#birthday-scraper)       | Nothing                 | Sqlite database                 | Gets all students birthdates |

---

## 🛠 Tools

### All Timetables

<img width="822" height="386" alt="image" src="https://github.com/user-attachments/assets/3c8d0f30-1761-4316-8a9a-eefae140e681" />


**Description:**  
Fetches the timetable of **all classes in the school**, including **room numbers** and **teachers**, and exports it to **Excel** and **JSON** formats. Also provides an **interactive timetable viewer** for easy browsing.

**What You Need:**

- An active Kisnapló account (uses **KSNPLSID – session ID**)
    
- [Guide on obtaining your KSNPLSID](#how-to-get-your-ksnplsid)
    

**How to Use:**  
```bash
cd all-timetables
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

python main.py
```

**How It Works:**  
The code works by exploiting the 'terem csere' room swap page and its contents, and reformats them into timetables

---

### Birthday Scraper

<img width="602" height="131" alt="image" src="https://github.com/user-attachments/assets/30098394-a3ea-4ca8-835a-26160f70af6c" />

**Description:**  
Extracts **every student’s birthdate, class, and age** from the Kisnapló system. Note: For complete coverage, the script should be run **continuously or periodically throughout the year**. See `how to run.txt` for more details.

**What You Need:**

- Nothing
    

**How to Use:**  
To effectively rebuild the whole database you would need to run the code every day for help on this please see the `how_to_use.txt` file

This is how to run manually:
```bash
cd birthday-scraper
python3 -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt

python main.py
```

**How It Works:**  
The code works by expoiting the 'whos birthday is today' functionality, which revels these informations about the student for that one day, doing this scrape daily, with for example a vps you can rebuild the database


## How to Get Your KSNPLSID

**What is a KSNPLSID?**  
The **KSNPLSID** is a short-lived session ID that allows the toolkit to access restricted data on Kisnapló. Some tools will prompt you to enter it when running.

**How to Obtain It:**

1. Log in to your Kisnapló account.
    
2. Look at the **end of the URL** in your browser. Your KSNPLSID will be there.

	<img width="937" height="229" alt="image" src="https://github.com/user-attachments/assets/cc6f25a1-974c-4404-94e3-09e400e77fb3" />


**Expiration:**

- The KSNPLSID is **temporary**.
    
- It expires **after a few minutes of inactivity** or roughly **one hour** automatically.
    
- You will need to obtain a **new KSNPLSID periodically** to continue using the toolkit.
    

