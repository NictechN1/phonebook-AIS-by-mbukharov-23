"""
МОДУЛЬНОЕ ТЕСТИРОВАНИЕ
АИС "Телефонный справочник"
"""

import unittest
import os
import sqlite3
from database import Database

class TestPhoneBook(unittest.TestCase):
    
    def setUp(self):
        """Настройка тестовой базы данных"""
        self.test_db = "test_phonebook.db"
        self.db = Database(self.test_db)
        self.db.connect()
        self.db.create_tables()
    
    def tearDown(self):
        """Очистка после тестов"""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
    
    def test_database_connection(self):
        """Тест подключения к базе данных"""
        self.assertIsNotNone(self.db.connection)
        print("✅ Тест подключения к БД пройден")
    
    def test_create_tables(self):
        """Тест создания таблиц"""
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'")
        table_exists = cursor.fetchone()
        self.assertIsNotNone(table_exists)
        print("✅ Тест создания таблиц пройден")
    
    def test_add_contact(self):
        """Тест добавления контакта"""
        cursor = self.db.connection.cursor()
        cursor.execute('''
            INSERT INTO contacts (first_name, last_name, phone, email, organization)
            VALUES (?, ?, ?, ?, ?)
        ''', ("Test", "User", "+79990000000", "test@test.com", "Test Org"))
        
        self.db.connection.commit()
        
        cursor.execute("SELECT COUNT(*) FROM contacts")
        count = cursor.fetchone()[0]
        self.assertEqual(count, 1)
        print("✅ Тест добавления контакта пройден")
    
    def test_search_contacts(self):
        """Тест поиска контактов"""
        # Добавляем тестовые данные
        cursor = self.db.connection.cursor()
        cursor.execute('''
            INSERT INTO contacts (first_name, last_name, phone, email, organization)
            VALUES (?, ?, ?, ?, ?)
        ''', ("Иван", "Иванов", "+79991111111", "ivan@mail.ru", "РАНХиГС"))
        
        # Ищем контакт
        cursor.execute('''
            SELECT * FROM contacts WHERE first_name LIKE ? OR last_name LIKE ?
        ''', ('%Иван%', '%Иван%'))
        
        results = cursor.fetchall()
        self.assertEqual(len(results), 1)
        print("✅ Тест поиска контактов пройден")

def run_tests():
    """Запуск всех тестов"""
    print("🚀 ЗАПУСК МОДУЛЬНЫХ ТЕСТОВ")
    print("=" * 40)
    
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestPhoneBook)
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    print("=" * 40)
    print(f"📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ:")
    print(f"✅ Пройдено: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Провалено: {len(result.failures)}")
    print(f"⚠️  Ошибок: {len(result.errors)}")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    run_tests()