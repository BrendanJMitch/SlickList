@ECHO OFF
:: Execute all unit tests on Windows.

cd "%~dp0/.."
ECHO Testing SlickList server...
python -m unittest

pause