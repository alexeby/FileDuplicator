rmdir /s /q dist 
pyinstaller --onefile main.py
mkdir dist\in\
mkdir dist\out\
mkdir dist\setup\
copy setup\conf.ini dist\setup