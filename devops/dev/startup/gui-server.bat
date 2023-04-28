cd C:\xampp\htdocs\files\wmiys\wmiys\src

set flask_program=C:\xampp\htdocs\files\wmiys\wmiys\.venv\Scripts\flask
set FLASK_DEBUG=true
set FLASK_APP=wmiys.gui

%flask_program% run --with-threads --host 0.0.0.0 --port 8000