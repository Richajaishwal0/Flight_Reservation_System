#  For creating and using a database

```bash
CREATE DATABASE flight_management;
USE flight_management;
```
# Creating a table
``` bash
CREATE TABLE available_flights (
flight_number VARCHAR(10) PRIMARY KEY,
start VARCHAR(50),
destination VARCHAR(50),
price DECIMAL(10, 2));

CREATE TABLE booked_flights (
booking_id INT AUTO_INCREMENT PRIMARY KEY,
flight_number VARCHAR(10),
user_name VARCHAR(50),
FOREIGN KEY (flight_number) REFERENCES available_flights(flight_number));
```
## Screenshot for sql command
![image](https://github.com/user-attachments/assets/3bc6e320-e824-4684-8bdc-08fbd7425576)
