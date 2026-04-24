import sqlite3
import os

DB_PATH = "profiles.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            category TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_category(age):
    if age <= 12:
        return "Criança"
    elif age <= 17:
        return "Adolescente"
    else:
        return "Adulto"

def save_profile(name, age):
    category = get_category(age)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO profiles (name, age, category) VALUES (?, ?, ?)",
        (name, age, category)
    )
    profile_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return profile_id, category

def get_profiles():
    if not os.path.exists(DB_PATH):
        init_db()
        return []
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, category FROM profiles ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "age": r[2], "category": r[3]} for r in rows]

def get_profile_by_id(profile_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, category FROM profiles WHERE id = ?", (profile_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "name": row[1], "age": row[2], "category": row[3]}
    return None

def delete_profile(profile_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM profiles WHERE id = ?", (profile_id,))
    conn.commit()
    conn.close()
    return True

def update_profile(profile_id, name, age):
    category = get_category(age)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE profiles SET name = ?, age = ?, category = ? WHERE id = ?",
        (name, age, category, profile_id)
    )
    conn.commit()
    conn.close()
    return True

# Initialize on import
init_db()
