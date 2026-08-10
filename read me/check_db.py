import sqlite3

conn = sqlite3.connect('db/predictions.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in database:", tables)

if tables:
    cursor.execute("PRAGMA table_info(predictions)")
    columns = cursor.fetchall()
    print("\nColumns in predictions table:")
    for col in columns:
        print(f"  - {col[1]} ({col[2]})")

conn.close()
print("\n✓ Database check complete!")
