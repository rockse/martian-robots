# Martian Robots
The Red Badger Robot Challenge 


## Steps to run 
- Install virtualenv: `python3 -m venv venv`
- Activate virtualenv: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Run bot: `python bot.py`
- Run tests: `python test_bot.py`
- Exit: Use `Control+C` (your OS interrupt key)

## Some major features
- Used numpy for grid
- Oritentation class can be extended for new turns and can be re-used
- Multiple Validation on classes and user input
- Logic and loops are pythonic

 ## Notes
- Wanted to add validation is `Machine` is off-grid initially using getter, setter as in `Planet`
- Wanted to add more tests for validators and mock data in a file
- Wanted to refactor some validations, also wanted to keep all validation messages in a single file
- Spent roughly ~3.5hrs. Haven't used click much in the past so needed to read some docs

**PS: Recommended to run on Python 3.7 or atleast Python 3.3**