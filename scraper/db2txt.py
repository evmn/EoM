import sqlite3
import csv

def save_to_file(cursor, output_file):
    with open(output_file, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write the header (column names)
        column_names = [description[0] for description in cursor.description]
        csv_writer.writerow(column_names)
        
        # Write the data (rows)
        for row in cursor.fetchall():
            csv_writer.writerow(row)

# Connect to the SQLite database
eom_db = "test.db"
connection = sqlite3.connect(eom_db)

output_file = "entries.txt"
# Execute the query
cursor = connection.cursor()
query = "select src from latex order by eid;"
#query = "select eid, entry.name latex.src from latex inner join entry where entry.id = latex.eid order by eid"
cursor.execute(query)

save_to_file(cursor, output_file)
# Close the connection
connection.close()
