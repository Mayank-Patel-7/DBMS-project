import mysql.connector 

def main():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='mayank@7',
            database='iste'
        )
        my_cursor = conn.cursor()
        
        if conn.is_connected():
            print("Connection established...")
            name = input("Enter Your Name: ")
            branch = input("Enter your Branch: ")
            year = input("Enter Your Year: ")
            skills = input("Enter Your Skills: ")
            phone = input("Enter your Contact no: ")  # This should be a string since you're using TEXT for other fields

            # SQL statement with the correct table name and placeholders
            s = 'INSERT INTO organizers (Name, Branch, Year, Skills, `Contact no.`) VALUES (%s, %s, %s, %s, %s)'

            # Execute the SQL statement with the parameters
            my_cursor.execute(s, (name, branch, year, skills, phone))  # Ensure this is a tuple of five elements
            conn.commit()
            print("Data Entered Successfully")

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        if conn.is_connected():
            conn.close()  # Ensure the connection is closed

if __name__ == "__main__":
    main()