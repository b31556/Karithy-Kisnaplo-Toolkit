import regex as re
import json
import requests
import datetime
import pandas as pd

ksnplsid= input("Enter your KSNPLSID: ")
url = f"https://kisnaplo.karinthy.hu/app/interface.php?view=v_roomplan&day=<DATE>&KSNPLSID={ksnplsid}"


def next_monday():
    today = datetime.date.today()
    days_ahead = 0 - today.weekday() + 7  # Monday is 0
    if days_ahead == 0:  # If today is Monday
        days_ahead = 7
    return today + datetime.timedelta(days=days_ahead)

print("Fetching timetables for the next week...")

week_timetables = {}

for i in range(5):
    date = next_monday() + datetime.timedelta(days=i)
    our_url = url.replace("<DATE>", str(date))

    response = requests.get(our_url)
    html_content = response.text

    pattern = r"data\.addRows\(([\s\S]*?)\]\);"
    match = re.findall(pattern, html_content, re.DOTALL)

    timetables = {}

    for math in match:
        if not math:
            raise ValueError("No match found, check KSNPLSID is valid and the page structure hasn't changed.")

        json_data = math + "]"
        json_data = json_data.replace("\n", " ").replace("\r", " ").replace("\t", " ").replace("'", 'äää').replace('"', "'").replace("äää", '"')
        json_data = json_data.replace("wi,", "").replace("sp,", "")
        json_data = re.sub(r",\s*\]", "]", json_data)
        data = json.loads(json_data)
        data=data[0]

        room = data.pop(0)
        room = room.split(" ")[-1].strip()

        classes = {}

        for entry in data:
            if not entry:
                continue
            if entry[0] == "[":
                
                hour = entry[2]

                if "szabad" in entry:
                    classes[hour] = {
                        "teacher": None,
                        "classes": []
                    }
                    continue

                if not "–" in entry: 
                    info = entry[5:].strip()
                    classes[hour] = {
                        "teacher": info,
                        "classes": ["special"]
                    }
                    continue
                techer,classess = entry[5:].split("–", 1)
                clas = classess.strip().split(",")

                classes[hour] = {
                    "teacher": techer,
                    "classes": clas
                }

        timetables[room] = classes
    week_timetables[date.strftime("%A")] = timetables

print("Processing timetables...")

TIMETABLES={}

try:
    for day, rooms in week_timetables.items():
        for room, classes in rooms.items():
            for hour, details in classes.items():
                if details["classes"]:
                    for clas in details["classes"]:
                        if clas not in TIMETABLES:
                            TIMETABLES[clas] = {}
                        if day not in TIMETABLES[clas]:
                            TIMETABLES[clas][day] = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": []}
                        if len(details["classes"]) > 1:
                            with_clas = [c for c in details["classes"] if c != clas]
                        TIMETABLES[clas][day][hour].append({
                            "room": room,
                            "teacher": details["teacher"],
                            "with": with_clas if len(details["classes"]) > 1 else []
                        })
except Exception as e:
    print(f"[ERROR] Failed to process timetables: {e}")

print("Saving timetables...")

try:
    with open("timetables.json", "w", encoding="utf-8") as f:
        json.dump(TIMETABLES, f, ensure_ascii=False, indent=4)

    print("Timetables saved to timetables.json")
except Exception as e:
    print(f"[ERROR] Failed to save timetables: {e}")

print("Creating Excel timetable...")

try:
    days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    with pd.ExcelWriter("timetables.xlsx") as writer:
        for clas, days in TIMETABLES.items():
            df = pd.DataFrame(index=[str(i) for i in range(9)], columns=days_order)
            for day in days_order:
                for hour in range(9):
                    entries = days.get(day, {}).get(str(hour), [])
                    if entries:
                        cell_text = []
                        for entry in entries:
                            cell_text.append(f"{entry['room']}  -  {entry['teacher']}")
                        df.at[str(hour), day] = " | ".join(cell_text)
                    else:
                        df.at[str(hour), day] = ""
            df.to_excel(writer, sheet_name=clas)

    print("Excel timetable saved as timetables.xlsx")
except Exception as e:
    print(f"[ERROR] Failed to create Excel file: {e}")


print("Done.")

print("You can view timetables for specific classes below.")
print(f"Available classes: {', '.join(TIMETABLES.keys())}")

while True:
    clas = input("Enter class to view timetable (or 'exit' to quit): ")
    if clas.lower() == "exit":
        break
    if clas in TIMETABLES:
        print(f"Timetable for class {clas}:")
        for day, hours in TIMETABLES[clas].items():
            print(f"  {day}:")
            for hour, entries in hours.items():
                if entries:
                    for entry in entries:
                        with_info = f" (with {', '.join(entry['with'])})" if entry['with'] else ""
                        print(f"    Hour {hour}: Room {entry['room']}, Teacher {entry['teacher']}{with_info}")
                else:
                    print(f"    Hour {hour}: No class")
    else:
        print(f"No timetable found for class {clas}.")