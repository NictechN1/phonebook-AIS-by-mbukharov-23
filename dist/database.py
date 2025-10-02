# database.py
import sqlite3
import os
import sys

def get_db_path():
    """Определяет правильный путь к базе данных"""
    if getattr(sys, 'frozen', False):
        # Если программа запущена как exe-файл
        base_path = os.path.dirname(sys.executable)
    else:
        # Если программа запущена из исходного кода
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, 'phonebook.db')

class Database:
    def __init__(self):
        db_path = get_db_path()
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    # остальные методы остаются без изменений...
    def add_contact(self, name, phone):
        self.cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
        self.conn.commit()
    
    def get_contacts(self):
        self.cursor.execute('SELECT * FROM contacts')
        return self.cursor.fetchall()
    
    def search_contacts(self, search_term):
        self.cursor.execute('SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?', 
                           (f'%{search_term}%', f'%{search_term}%'))
        return self.cursor.fetchall()
    
    def update_contact(self, contact_id, name, phone):
        self.cursor.execute('UPDATE contacts SET name=?, phone=? WHERE id=?', (name, phone, contact_id))
        self.conn.commit()
    
    def delete_contact(self, contact_id):
        self.cursor.execute('DELETE FROM contacts WHERE id=?', (contact_id,))
        self.conn.commit()