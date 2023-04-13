import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Set the path to the database file
database_path = 'vandalism.db'

# Connect to the database
conn = sqlite3.connect(database_path)

# Retrieve first 5 rows from vandalism table
q_head = 'SELECT * FROM vandalism LIMIT 5'
df = pd.read_sql_query(q_head, conn)

# Retrieve a table that shows vandalism by zip code
q_vandalism_zip = 'SELECT COUNT(*) AS count, zip FROM vandalism GROUP BY zip ORDER BY count DESC LIMIT 5'
vandalism_zip = pd.read_sql_query(q_vandalism_zip, conn)

# Close the database connection
conn.close()

print(vandalism_zip)
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(vandalism_zip['zip'], vandalism_zip['count'].values)
ax.set_xlabel('Zip Code')
ax.set_ylabel('Count')
ax.set_title('Vandalism by Zip Code')
plt.show()