import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Establishing a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="richa@2006",  # Update this with your correct password
    database="flight_management"
)
cursor = conn.cursor()

# Creating necessary tables if they do not exist
cursor.execute("CREATE TABLE IF NOT EXISTS available_flights (flight_number VARCHAR(10), start VARCHAR(50), destination VARCHAR(50), price FLOAT)")
cursor.execute("CREATE TABLE IF NOT EXISTS booked_flights (booking_id INT AUTO_INCREMENT PRIMARY KEY, flight_number VARCHAR(10), user_name VARCHAR(50))")

# Sample flight data
cursor.execute("DELETE FROM available_flights")  # Clearing previous data
cursor.executemany(
    "INSERT INTO available_flights (flight_number, start, destination, price) VALUES (%s, %s, %s, %s)",
    [
        ("FL001", "New York", "Los Angeles", 150.00),
        ("FL002", "Chicago", "Houston", 120.00),
        ("FL003", "San Francisco", "Seattle", 90.00),
        ("FL004", "Miami", "Atlanta", 110.00),
        ("FL005", "Boston", "Philadelphia", 130.00),
        ("FL006", "Dallas", "San Diego", 140.00),
        ("FL007", "Washington DC", "Denver", 160.00),
        ("FL008", "San Jose", "Las Vegas", 100.00),
        ("FL009", "Austin", "San Antonio", 80.00),
        ("FL010", "Seattle", "Portland", 70.00),
        ("FL011", "New Orleans", "Memphis", 90.00),
        ("FL012", "Orlando", "Tampa", 85.00)
    ]
)
conn.commit()

# Function to refresh the available flights table
def refresh_available_flights():
    for row in available_flights_table.get_children():
        available_flights_table.delete(row)
    cursor.execute("SELECT * FROM available_flights")
    for flight in cursor.fetchall():
        available_flights_table.insert("", "end", values=flight)

# Function to refresh the booked flights table
def refresh_booked_flights():
    for row in booked_flights_table.get_children():
        booked_flights_table.delete(row)
    cursor.execute("SELECT booking_id, flight_number, user_name FROM booked_flights")
    for booking in cursor.fetchall():
        booked_flights_table.insert("", "end", values=booking)

# Function to handle booking a flight
def book_flight():
    selected_flight = available_flights_table.selection()
    user_name = name_entry.get()
    if selected_flight and user_name:
        flight = available_flights_table.item(selected_flight[0])['values']
        cursor.execute("INSERT INTO booked_flights (flight_number, user_name) VALUES (%s, %s)", (flight[0], user_name))
        conn.commit()
        refresh_booked_flights()
        messagebox.showinfo("Success", f"Flight {flight[0]} booked successfully for {user_name}!")
    else:
        messagebox.showerror("Error", "Please select a flight and enter your name.")

# Function to handle booking cancellation
def cancel_booking():
    selected_booking = booked_flights_table.selection()
    if selected_booking:
        booking_id = booked_flights_table.item(selected_booking[0])['values'][0]
        cursor.execute("DELETE FROM booked_flights WHERE booking_id = %s", (booking_id,))
        conn.commit()
        refresh_booked_flights()
        messagebox.showinfo("Success", "Booking canceled successfully!")
    else:
        messagebox.showerror("Error", "Please select a booking to cancel.")

# Tkinter main window setup
root = tk.Tk()
root.title("Flight Management System")
root.geometry("1200x700")
root.configure(bg="#F0F4F8")  # Light background color

# Styling for tables and general UI
style = ttk.Style()
style.configure("Treeview", background="#E0E0E0", foreground="black", rowheight=30, fieldbackground="#E0E0E0", font=("Arial", 12))
style.map("Treeview", background=[("selected", "#6C63FF")], foreground=[("selected", "white")])

# Available Flights Label Frame
available_frame = tk.LabelFrame(root, text="Available Flights", bg="#4A4E69", fg="white", font=("Arial", 14, "bold"), padx=10, pady=10)
available_frame.place(x=20, y=20, width=1150, height=300)

# Available Flights Table
available_flights_table = ttk.Treeview(available_frame, columns=("Flight Number", "Start", "Destination", "Price"), show="headings")
available_flights_table.heading("Flight Number", text="Flight Number")
available_flights_table.heading("Start", text="Start")
available_flights_table.heading("Destination", text="Destination")
available_flights_table.heading("Price", text="Price")
available_flights_table.pack(fill=tk.BOTH, expand=True)
refresh_available_flights()

# Booked Flights Label Frame
booked_frame = tk.LabelFrame(root, text="Booked Flights", bg="#4A4E69", fg="white", font=("Arial", 14, "bold"), padx=10, pady=10)
booked_frame.place(x=20, y=340, width=1150, height=300)

# Booked Flights Table
booked_flights_table = ttk.Treeview(booked_frame, columns=("Booking ID", "Flight Number", "User Name"), show="headings")
booked_flights_table.heading("Booking ID", text="Booking ID")
booked_flights_table.heading("Flight Number", text="Flight Number")
booked_flights_table.heading("User Name", text="User Name")
booked_flights_table.pack(fill=tk.BOTH, expand=True)
refresh_booked_flights()

# User Name Entry and Book Flight Button
name_label = tk.Label(root, text="Enter Your Name:", bg="#F0F4F8", font=("Arial", 12))
name_label.place(x=20, y=650)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.place(x=150, y=650, width=200)

book_button = tk.Button(root, text="Book Flight", bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), command=book_flight)
book_button.place(x=370, y=645, width=150)

# Cancel Booking Button
cancel_button = tk.Button(root, text="Cancel Booking", bg="#F44336", fg="white", font=("Arial", 12, "bold"), command=cancel_booking)
cancel_button.place(x=550, y=645, width=150)

root.mainloop()

# Close database connection when program ends
conn.close()
