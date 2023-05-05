import requests
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# API endpoint and parameters for getting prayer times for Alexandria, Egypt
url = "http://api.aladhan.com/v1/timingsByCity"
params = {
    "city": "Alexandria",
    "country": "Egypt",
    "method": 5, # Egyptian General Authority of Survey
    "latitude": 31.2001,
    "longitude": 29.9187,
    "timezone": 2,
    "school": 0 # Shafi'i
}

statue = "Updated automatically every 12 hours!"
# Create the root window
root = tk.Tk()
root.title("Muslim Prayer Times")
root.geometry("400x450+120+50")
root.resizable(False, False)

# Set the background color
root.configure(bg="#1c1c1c")

# Create the header label
header_label = ttk.Label(root, text="Muslim Prayer Times", font=("Algerian", 20), foreground="#d6d6d6", background="#1c1c1c")
header_label.pack(pady=(20,0))

# Create the frame for the prayer time labels
style = ttk.Style()
style.configure("CustomFrame.TFrame", background="black")
prayer_frame = ttk.Frame(root, borderwidth=5, relief="solid", style="CustomFrame.TFrame", height=root.winfo_height(), width=root.winfo_width())
prayer_frame.pack(pady=(30,50))


# set the font for the labels
label_font = ("Algerian", 15)
label_font2 = ("Algerian", 18)

# add some padding to the labels
width = 10
pady = 5

# create labels for each prayer name with a specific x and y position, and larger font
tk.Label(prayer_frame, text="Fajr", font=label_font, width=width, pady=pady, background="#f2c26b").grid(row=0, column=0, padx=10, pady=10)
tk.Label(prayer_frame, text="Dhuhr", font=label_font,width=width, pady=pady, background="#e8a761").grid(row=1, column=0, padx=10, pady=10)
tk.Label(prayer_frame, text="Asr", font=label_font,width=width, pady=pady, background="#e4926d").grid(row=2, column=0, padx=10, pady=10)
tk.Label(prayer_frame, text="Maghrib", font=label_font,width=width, pady=pady, background="#d9755a").grid(row=3, column=0, padx=10, pady=10)
tk.Label(prayer_frame, text="Isha", font=label_font,width=width, pady=pady, background="#c94c4c").grid(row=4, column=0, padx=10, pady=10)


# Create the prayer time labels
text = "Updating.."
fajr_label = ttk.Label(prayer_frame, text=text, font=label_font2, foreground="#1c1c1c", background="#d6d6d6", width=10)
fajr_label.grid(row=0, column=1, padx=10, pady=10)


dhuhr_label = ttk.Label(prayer_frame, text=text, font=label_font2, foreground="#1c1c1c", background="#d6d6d6", width=10)
dhuhr_label.grid(row=1, column=1, padx=10, pady=10)

asr_label = ttk.Label(prayer_frame, text=text, font=label_font2, foreground="#1c1c1c", background="#d6d6d6", width=10)
asr_label.grid(row=2, column=1, padx=10, pady=10)

maghrib_label = ttk.Label(prayer_frame, text=text, font=label_font2, foreground="#1c1c1c", background="#d6d6d6", width=10)
maghrib_label.grid(row=3, column=1, padx=10, pady=10)

isha_label = ttk.Label(prayer_frame, text=text, font=label_font2, foreground="#1c1c1c", background="#d6d6d6", width=10)
isha_label.grid(row=4, column=1, padx=10, pady=10)


# Function to get the current prayer times from the API
def get_prayer_times():
    global statue 
    try:
        response = requests.get(url, params=params)
        statue = "Updated automatically every 12 hours!"
        print(response.text)
        data = response.json()["data"]
        times = data["timings"]
        prayer_times = {
            "Fajr": times["Fajr"],
            "Dhuhr": times["Dhuhr"],
            "Asr": times["Asr"],
            "Maghrib": times["Maghrib"],
            "Isha": times["Isha"]
        }
        return prayer_times
    except:
        print("error in internet")
        statue="Error with connection to the internet!"





# Function to update the prayer time labels
def update_prayer_times():
    print("Updating prayer times...")
    prayer_times = get_prayer_times()
    fajr_label.config(text=prayer_times["Fajr"])
    dhuhr_label.config(text=prayer_times["Dhuhr"])
    asr_label.config(text=prayer_times["Asr"])
    maghrib_label.config(text=prayer_times["Maghrib"])
    isha_label.config(text=prayer_times["Isha"])
    # Schedule the function to run again in 12 hours
    root.after(43200000, update_prayer_times)

def modify_update_prayer_times():
    try:
        prayer_times = get_prayer_times()
        fajr_label.config(text=prayer_times["Fajr"])
        dhuhr_label.config(text=prayer_times["Dhuhr"])
        asr_label.config(text=prayer_times["Asr"])
        maghrib_label.config(text=prayer_times["Maghrib"])
        isha_label.config(text=prayer_times["Isha"])
    except:
        print("error in updating the timing due to the error in the internet!")
        print("Updating prayer times...")







def refresh_button_clicked():
    # function to handle the refresh button click event
    refresh_btn.config(state="disabled", text="Updating...") # disable button and change text
    modify_update_prayer_times()
    refresh_btn.config(state="normal", text="Update Prayer Times") # re-enable button and change text back


# create the refresh button
refresh_btn = tk.Button(root, text="Update Prayer Times",font=("Algerian", 10), command=refresh_button_clicked)
refresh_btn.place(x=130, y=390)

# change the button color
refresh_btn.config(bg="gray", fg="black")


footer_label = ttk.Label(root, text=statue, font=("Helvetica", 10), foreground="#d6d6d6", background="#1c1c1c")
footer_label.pack(side="bottom", pady=(0,10))

root.after(43200000, update_prayer_times)

root.mainloop()