### 
### Max Auto Clicker (Mac OS release)
###
### Wbesite: https://maxautoclicker.blogspot.com/
###
### Version: 1.0.1
###

import tkinter as tk
import pyautogui #
import time
import keyboard #

should_continue_clicking = False


def start_clicking():
    global should_continue_clicking

    # Get the mouse button
    button = button_var.get()

    # Get the click type
    click_type = click_type_var.get()

    # Get the number of clicks or check if it's unlimited
    num_clicks = clicks_entry.get()
    if num_clicks.lower() == 'unlimited':
        num_clicks = float('inf')
    else:
        num_clicks = int(num_clicks)

    # Get the click interval
    interval = float(interval_entry.get())

    # Get the click location
    #x = int(x_entry.get())
    #y = int(y_entry.get())
    #click_location = (x, y)

    # Perform the clicks
    i = 0
    while i < num_clicks and should_continue_clicking:
    # Get the click location
        click_location = pyautogui.position()
        if button == "Left":
            if click_type == "Single":
                pyautogui.click(click_location, button="left")
            elif click_type == "Double":
                pyautogui.doubleClick(click_location, button="left")
            elif click_type == "Hold":
                pyautogui.mouseDown(click_location, button="left")
        elif button == "Middle":
            if click_type == "Single":
                pyautogui.click(click_location, button="Middle")
            elif click_type == "Double":
                pyautogui.doubleClick(click_location, button="Middle")
            elif click_type == "Hold":
                pyautogui.mouseDown(click_location, button="Middle")
        elif button == "Right":
            if click_type == "Single":
                pyautogui.click(click_location, button="right")
            elif click_type == "Double":
                pyautogui.doubleClick(click_location, button="right")
            elif click_type == "Hold":
                pyautogui.mouseDown(click_location, button="right")

        root.update()
        time.sleep(interval/1000.0)
        i += 1
    should_continue_clicking = False


def on_hotkey_start():
    global should_continue_clicking
    should_continue_clicking = True
    start_clicking()

 
def on_hotkey_stop():
    global should_continue_clicking
    should_continue_clicking = False



# Create the GUI window
root = tk.Tk()
root.title("Max Auto Clicker")

# Set the size of the window
root.geometry("270x300")

# Create the label and combobox for the mouse button
button_var = tk.StringVar()
button_var.set("Left")  # set the default mouse button to "Left"
mouse_button_label = tk.Label(root, text="Mouse button:")
mouse_button_label.config(font=('Arial', 11, 'bold'))
mouse_button_label.pack(pady=5)
mouse_button_combo = tk.ttk.Combobox(root, textvariable=button_var, values=["Left", "Middle", "Right"])
mouse_button_combo.pack()

# Create the label and combobox for the click type
click_type_var = tk.StringVar()
click_type_var.set("Single")  # set the default click type to "Single"
click_type_label = tk.Label(root, text="Click type:")
click_type_label.config(font=('Arial', 11, 'bold'))
click_type_label.pack(pady=5)
click_type_combo = tk.ttk.Combobox(root, textvariable=click_type_var, values=["Single", "Double", "Hold"])
click_type_combo.pack()

# Create the label and entry widgets for the number of clicks
clicks_label = tk.Label(root, text="Number of clicks:")
clicks_label.config(font=('Arial', 11, 'bold'))
clicks_label.pack(pady=5)
clicks_entry = tk.Entry(root)
clicks_entry.insert(0, "20") # set the default number of clicks to 1
clicks_entry.pack()

# Create the label and entry widgets for the click interval
interval_label = tk.Label(root, text="Interval (ms):")
interval_label.config(font=('Arial', 11, 'bold'))
interval_label.pack(pady=5)
interval_entry = tk.Entry(root)
interval_entry.insert(0, "100") # set the default interval to 100 ms
interval_entry.pack()

# Create the label and entry widgets for the click location

#x_label = tk.Label(root, text="X:")
#x_label.config(font=('Arial', 11, 'bold'))
#x_label.pack()
#x_entry = tk.Entry(root)
#x_entry.insert(0, "675")
#x_entry.pack()

#y_label = tk.Label(root, text="Y:")
#x_label.config(font=('Arial', 11, 'bold'))
##y_label.pack()
#y_entry = tk.Entry(root)
#y_entry.insert(0, "415")
#y_entry.pack()

# Create the start button
start_button = tk.Button(root, text="Start", command=on_hotkey_start)
start_button.pack(pady=5)

# Create the stop label
clicks_label = tk.Label(root, text="Stop : [F6]")
clicks_label.pack()

# Register the hotkeys
#keyboard.add_hotkey('F5', on_hotkey_start)
keyboard.add_hotkey('F6', on_hotkey_stop)


# Start the GUI event loop
root.mainloop()
#keyboard.unhook_all()


