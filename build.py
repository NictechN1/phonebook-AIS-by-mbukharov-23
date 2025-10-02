# build.py
import os
import sys
import subprocess
import shutil

def install_pyinstaller():
    try:
        import PyInstaller
        print("✅ PyInstaller уже установлен")
    except ImportError:
        print("❌ PyInstaller не установлен. Устанавливаю...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller успешно установлен")

def build_executable():
    try:
        import PyInstaller.__main__
        
        # Если существует база данных, копируем её
        db_src = 'src/phonebook.db'
        if os.path.exists(db_src):
            shutil.copy(db_src, '.')
            print("✅ База данных скопирована в корень")
        
        params = [
            'src/main.py',
            '--name=Телефонный_справочник',
            '--onefile',
            '--windowed',
            '--add-data=src/database.py;.',
            '--add-data=src/gui.py;.',
            '--add-data=phonebook.db;.',  # добавляем базу данных
            '--clean',
            '--noconsole',
            '--distpath=.',
        ]
        
        print("🚀 Начинаю сборку исполняемого файла...")
        PyInstaller.__main__.run(params)
        
        if os.path.exists('Телефонный_справочник.exe'):
            print("✅ Исполняемый файл успешно создан!")
            
    except Exception as e:
        print(f"❌ Ошибка при сборке: {e}")

if __name__ == "__main__":
    install_pyinstaller()
    build_executable()
    input("\nНажмите Enter для выхода...")