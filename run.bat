

@echo off
call venv\scripts\activate
 pytest -v -s -m "sanity"  
pause