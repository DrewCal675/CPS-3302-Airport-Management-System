import sqlite3

def main():
    conn = sqlite3.connect('airport.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Passenger (
        PassengerID INTEGER PRIMARY KEY NOT NULL,
        FirstName TEXT,
        LastName TEXT
        )''')
        
    cur.execute('''CREATE TABLE IF NOT EXISTS Plane (
        PlaneID INTEGER PRIMARY KEY NOT NULL,
        Capacity INTEGER
        );''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Flight (
        FlightID INTEGER PRIMARY KEY NOT NULL,
        Time TEXT,
        Destination TEXT,
        PlaneID INTEGER REFERENCES Plane(PlaneID)
        )''')
        
    cur.execute('''CREATE TABLE IF NOT EXISTS Ticket (
        TicketID INTEGER PRIMARY KEY NOT NULL,
        PassengerID INTEGER REFERENCES Passenger(PassengerID),
        FlightID INTEGER REFERENCES Flight(FlightID))''')
    
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()