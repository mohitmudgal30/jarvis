@echo off

set INTERVAL=10
:loop
E:
cd  E:\7th ai\ai\jarvis-master
python ja2.py
timeout %INTERVAL%
goto:loop