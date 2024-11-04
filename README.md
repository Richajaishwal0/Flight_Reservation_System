# Flight Reservation System

This is a Flight Reservation System built with Python's `tkinter` library for the GUI and MySQL as the backend database. The application allows users to view available flights, book a flight, and cancel bookings.

## Features

- **View Available Flights**: Displays a list of all available flights with details like flight number, start location, destination, and price.
- **Book Flights**: Users can book a flight by selecting an available flight and entering their name.
- **Cancel Bookings**: Users can cancel an existing booking.
- **MySQL Database Integration**: Flight and booking information is stored and managed through MySQL.

## Requirements

- Python 3.x
- MySQL Server
- Python Libraries:
  - `tkinter`
  - `mysql-connector-python`

## Setup

1. **Clone the Repository after creating the fork** :
   ```bash
   git clone https://github.com/your-username/flight-management-system.git
   cd flight-management-system
   ```

2. **Install Dependencies**:
   Ensure `mysql-connector-python` is installed:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set Up MySQL Database**:
   - Create a new database called `flight_management`.
   - Create two tables: `available_flights` and `booked_flights`.

   Run the following commands in your MySQL shell:

   ```sql
   CREATE DATABASE flight_management;
   USE flight_management;

   CREATE TABLE available_flights (
       flight_number VARCHAR(10),
       start VARCHAR(50),
       destination VARCHAR(50),
       price FLOAT
   );

   CREATE TABLE booked_flights (
       booking_id INT AUTO_INCREMENT PRIMARY KEY,
       flight_number VARCHAR(10),
       user_name VARCHAR(50)
   );
   ```

4. **Update Database Credentials**:
   Open the Python script and replace the MySQL connection parameters (host, user, password) with your own MySQL credentials:

   ```python
   conn = mysql.connector.connect(
       host="localhost",
       user="your_mysql_username",
       password="your_mysql_password",
       database="flight_management"
   )
   ```

5. **Run the Application**:
   Execute the Python script:
   ```bash
   python flight_management_system.py
   ```

## Usage

1. **View Available Flights**: When the application starts, it loads available flights into the `Available Flights` table.

2. **Book a Flight**:
   - Enter your name in the "Enter Your Name" field.
   - Select a flight from the `Available Flights` table.
   - Click the "Book Flight" button to confirm the booking.
   - The booking will appear in the `Booked Flights` table.

3. **Cancel a Booking**:
   - Select a booking from the `Booked Flights` table.
   - Click the "Cancel Booking" button to delete the booking.

## Project Structure
```plaintext
Flight_Reservation_System/
│
├── Flight_reservation.py  # Main application code
├── MYSQL.md               # MySQL setup and configuration documentation
├── Output.md              # Expected output or usage examples
└── README.md              # Project documentation (main README file)
```

## Screenshots

![Available Flights](https://github.com/user-attachments/assets/9b248fa8-cef2-4901-852e-abc839f9fb05)

*Screenshot showing the available flights.*

![Booked Flights](https://github.com/user-attachments/assets/3c69edb0-7d71-4d39-b593-32bfd3b0c7f0)

*Screenshot showing booked flights after a booking.*

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Python’s `tkinter` library](https://docs.python.org/3/library/tkinter.html) for the GUI.
- [MySQL](https://www.mysql.com/) for database management.
- Sample flight data to demonstrate the booking system.

---

