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

- [[#📊 Charts What You Need / Tool Use]]
    
- [[#🛠 Tools]]
    
    - [[#All Timetables]]
        
    - [[#Birthday Scraper]]
    
-  [[#How to Get Your KSNPLID]]

---

## 📊 Charts: What You Need / Tool Use

| Tool                                                                                            | What You Need           | Output                          | What it does                 |
| ----------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------- | ---------------------------- |
| [All Timetables](https://chatgpt.com/c/68bdc2cf-9ff8-832f-bd1b-00e7f69e1559#all-timetables)     | Active Kisnapló account | Excel, JSON, Interactive Viewer | Gets all clases timetables   |
| [Birthday Scraper](https://chatgpt.com/c/68bdc2cf-9ff8-832f-bd1b-00e7f69e1559#birthday-scraper) | Nothing                 | Sqlite database                 | Gets all students birthdates |

---

## 🛠 Tools

### All Timetables

![[Pasted image 20250907223403.png]]

**Description:**  
Fetches the timetable of **all classes in the school**, including **room numbers** and **teachers**, and exports it to **Excel** and **JSON** formats. Also provides an **interactive timetable viewer** for easy browsing.

**What You Need:**

- An active Kisnapló account (uses **KSNPLID – session ID**)
    
- [Guide on obtaining your KSNPLID](https://chatgpt.com/c/docs/how-to-get-ksnplid.md)
    

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

![[Pasted image 20250907223137.png]]

**Description:**  
Extracts **every student’s birthdate, class, and age** from the Kisnapló system. Note: For complete coverage, the script should be run **continuously or periodically throughout the year**. See [how to run.txt](https://chatgpt.com/c/docs/how-to-run.txt) for more details.

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


## How to Get Your KSNPLID

**What is a KSNPLID?**  
The **KSNPLID** is a short-lived session ID that allows the toolkit to access restricted data on Kisnapló. Some tools will prompt you to enter it when running.

**How to Obtain It:**

1. Log in to your Kisnapló account.
    
2. Look at the **end of the URL** in your browser. Your KSNPLID will be there.

	![[Pasted image 20250907223028.png]]

**Expiration:**

- The KSNPLID is **temporary**.
    
- It expires **after a few minutes of inactivity** or roughly **one hour** automatically.
    
- You will need to obtain a **new KSNPLID periodically** to continue using the toolkit.
    

