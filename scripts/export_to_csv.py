import sqlite3
import csv

# Connect to the SQLite database
eom_db = "test.db"
connection = sqlite3.connect(eom_db)

# Execute the query
cursor = connection.cursor()
query = "select src from latex order by eid;"
#query = "select eid, items.title latex.content from latex inner join items where items.id = latex.eid order by eid"
cursor.execute(query)

# Write the query result to a CSV file
with open("latex_content.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header (column names)
    column_names = [description[0] for description in cursor.description]
    csv_writer.writerow(column_names)
    
    # Write the data (rows)
    for row in cursor.fetchall():
        csv_writer.writerow(row)

# Close the connection
connection.close()

