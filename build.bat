rmdir /s /q dist ^
 & venv\Scripts\activate.bat ^
 && pyinstaller main.py -n="fileDuplicator" --onefile ^
 && venv\Scripts\deactivate.bat ^
 && mkdir dist\in\ ^
 && mkdir dist\out\ ^
 && mkdir dist\setup\ ^
 && mkdir dist\log\ ^
 && copy setup\conf.ini dist\setup ^
 && copy setup\log.ini dist\setup