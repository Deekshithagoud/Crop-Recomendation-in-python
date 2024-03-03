import tkinter as tk
from tkinter import messagebox

def on_crop_selection():
    soil_type = soil_var.get()
    water_availability = water_var.get()
    start_month = month_var.get()

    crop_recommendation = get_crop_recommendation(soil_type, water_availability, start_month)

    messagebox.showinfo("Crop Recommendation", f"The suitable crop for the given details is: {crop_recommendation}")

def get_crop_recommendation(soil_type, water_availability, start_month):
    if soil_type == 1 and water_availability == 1 and start_month == 1:
        return "Paddy"
    elif soil_type == 1 and water_availability == 1 and start_month == 2:
        return "Capsicum"
    elif soil_type == 1 and water_availability == 2 and start_month == 1:
        return "Sweet corn"
    elif soil_type == 1 and water_availability == 2 and start_month == 2:
        return "Sugarcane"
    elif soil_type == 2 and water_availability == 1 and start_month == 1:
        return "Cauli Flower"
    elif soil_type == 2 and water_availability == 1 and start_month == 2:
        return "Tomato"
    elif soil_type == 2 and water_availability == 2 and start_month == 1:
        return "Brinjal"
    elif soil_type == 2 and water_availability == 2 and start_month == 2:
        return "Potato"
    elif soil_type == 3 and water_availability == 1 and start_month == 1:
        return "Corriander"
    elif soil_type == 3 and water_availability == 1 and start_month == 2:
        return "carrot"
    elif soil_type == 3 and water_availability == 2 and start_month == 2:
        return "Beetroot"
    elif soil_type == 3 and water_availability == 2 and start_month == 1:
        return "Radish"
    
    # Add more crop recommendations for other conditions

# Create main window
window = tk.Tk()
window.title("Vaarahi Crop Advisor")

# Soil Type
soil_label = tk.Label(window, text="Select Soil Type:")
soil_var = tk.IntVar()
soil_var.set(1)  # Default value
soil_buttons = [
    ("Redsoil", 1),
    ("Blacksoil", 2),
    ("Chalkysoil", 3)
]
for text, value in soil_buttons:
    tk.Radiobutton(window, text=text, variable=soil_var, value=value).pack() 

# Water Availability
water_label = tk.Label(window, text="Water Availability:")
water_var = tk.IntVar()
water_var.set(1)  # Default value
water_buttons = [
    ("You Have Water Availability?", 1),
    ("YOu Dont have water facility", 2)
]
for text, value in water_buttons:
    tk.Radiobutton(window, text=text, variable=water_var, value=value).pack()

# Start Month
month_label = tk.Label(window, text="Select Start Month:")
month_var = tk.IntVar()
month_var.set(1)  # Default value
month_buttons = [
    ("Jan", 1),
    ("Feb", 2)
]
for text, value in month_buttons:
    tk.Radiobutton(window, text=text, variable=month_var, value=value).pack()

# Button to get recommendation
recommend_button = tk.Button(window, text="Get Crop Recommendation", command=on_crop_selection,bg="black",fg="yellow",width=20)
recommend_button.pack(padx=10,pady=10)


# Run the Tkinter event loop
window.mainloop()
