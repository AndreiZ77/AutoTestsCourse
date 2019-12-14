# Auto Tests Course
Homework at the Auto tests course Stepik (https://stepik.org/course/575)


The test_items.py checks the ability to add goods to the basket in the online store, when choosing different languages.

First of all, you need to install:

python 3.7

selenium

pytest



To start use the command line. Examples:

 pytest --browser_name=chrome --language=en test_*.py
 
 pytest --browser_name=firefox test_items.py
 
 pytest --language=es
 
For review main tests:
 
 pytest -v --tb=line --language=en -m need_review 

