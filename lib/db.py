import os
import sqlite3

# Try to import psycopg2 for Postgres (Vercel)
try:
    import psycopg2
    from psycopg2.extras import RealDictCursor
    HAS_POSTGRES = True
except ImportError:
    HAS_POSTGRES = False

IS_VERCEL = os.environ.get("VERCEL") == "1"
DB_PATH = "profiles.db"

def get_connection():
    if IS_VERCEL:
        # Connect to Vercel Postgres using the environment variable
        POSTGRES_URL = os.environ.get("POSTGRES_URL")
        # Use simple URL connection for psycopg2
        return psycopg2.connect(POSTGRES_URL)
    else:
        # Local SQLite
        return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    if IS_VERCEL:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS profiles (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                category TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS watched_videos (
                id SERIAL PRIMARY KEY,
                profile_id INTEGER REFERENCES profiles(id) ON DELETE CASCADE,
                video_id VARCHAR(100) NOT NULL,
                watched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(profile_id, video_id)
            )
        """)
    else:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                category TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS watched_videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                profile_id INTEGER REFERENCES profiles(id) ON DELETE CASCADE,
                video_id TEXT NOT NULL,
                watched_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(profile_id, video_id)
            )
        """)
    conn.commit()
    conn.close()

def get_category(age):
    if age <= 12: return "Criança"
    if age <= 17: return "Adolescente"
    return "Adulto"

def save_profile(name, age):
    category = get_category(age)
    conn = get_connection()
    cursor = conn.cursor()
    if IS_VERCEL:
        cursor.execute(
            "INSERT INTO profiles (name, age, category) VALUES (%s, %s, %s) RETURNING id",
            (name, age, category)
        )
        profile_id = cursor.fetchone()[0]
    else:
        cursor.execute(
            "INSERT INTO profiles (name, age, category) VALUES (?, ?, ?)",
            (name, age, category)
        )
        profile_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return profile_id, category

def get_profiles():
    conn = get_connection()
    if IS_VERCEL:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT id, name, age, category FROM profiles ORDER BY id DESC")
        rows = cursor.fetchall()
        profiles = [dict(row) for row in rows]
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, category FROM profiles ORDER BY id DESC")
        rows = cursor.fetchall()
        profiles = [{"id": r[0], "name": r[1], "age": r[2], "category": r[3]} for r in rows]
    conn.close()
    return profiles

def get_profile_by_id(profile_id):
    conn = get_connection()
    if IS_VERCEL:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT id, name, age, category FROM profiles WHERE id = %s", (profile_id,))
        row = cursor.fetchone()
        profile = dict(row) if row else None
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, category FROM profiles WHERE id = ?", (profile_id,))
        row = cursor.fetchone()
        profile = {"id": row[0], "name": row[1], "age": row[2], "category": row[3]} if row else None
    conn.close()
    return profile

def delete_profile(profile_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM profiles WHERE id = %s" if IS_VERCEL else "DELETE FROM profiles WHERE id = ?"
    cursor.execute(query, (profile_id,))
    conn.commit()
    conn.close()
    return True

def update_profile(profile_id, name, age):
    category = get_category(age)
    conn = get_connection()
    cursor = conn.cursor()
    if IS_VERCEL:
        cursor.execute(
            "UPDATE profiles SET name = %s, age = %s, category = %s WHERE id = %s",
            (name, age, category, profile_id)
        )
    else:
        cursor.execute(
            "UPDATE profiles SET name = ?, age = ?, category = ? WHERE id = ?",
            (name, age, category, profile_id)
        )
    conn.commit()
    conn.close()
    return True

def mark_as_watched(profile_id, video_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO watched_videos (profile_id, video_id) 
        VALUES (%s, %s) 
        ON CONFLICT (profile_id, video_id) DO NOTHING
    """ if IS_VERCEL else """
        INSERT OR IGNORE INTO watched_videos (profile_id, video_id) 
        VALUES (?, ?)
    """
    cursor.execute(query, (profile_id, video_id))
    conn.commit()
    conn.close()
    return True

def get_watched_video_ids(profile_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT video_id FROM watched_videos WHERE profile_id = %s" if IS_VERCEL else "SELECT video_id FROM watched_videos WHERE profile_id = ?"
    cursor.execute(query, (profile_id,))
    rows = cursor.fetchall()
    ids = [r[0] for r in rows]
    conn.close()
    return ids

# Initialize on import
try:
    init_db()
except Exception as e:
    print(f"DATABASE INIT ERROR (Might be missing Postgres URL on Vercel): {e}")

