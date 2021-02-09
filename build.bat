rmdir /s /q dist ^
 & venv\Scripts\activate.bat ^
 && pyinstaller main.py -n="fileDuplicator" --onefile ^
 && venv\Scripts\deactivate.bat ^
 && mkdir dist\in\ ^
 && mkdir dist\out\ ^
 && mkdir dist\setup\ ^
 && copy setup\conf.ini dist\setup