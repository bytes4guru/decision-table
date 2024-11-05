# Project Decision

This project utilizes a Decision Data Holder model to manage and store decision-related data.

## Proejct structured
app
├── models
│   ├── abstract.py
│   ├── condition.py
│   ├── decision_data_holder.py
│   ├── decision_table.py
├── tests
│   ├── test_decision_table.py
│   └── resources
│       └── scoring_process_result.csv
├── .env
├── Pipfile
├── README.txt
├── run_lint_check
└── setup.cfg

The decision_table.py file defines the DecisionTable class which is the main worker class of this project. It crates a decision table from a csv file and apply the rules to the give inputs
The condition.py file defines the condition class which is a main building block of decision table

## Environment setup
 - install python 3.9 (specified in the Pipfile file) if not installed already
 - install pipenv if not installed already
 - setup packages
      * start the virtual environment
            pipenv shell
      * install all dependencies
            pipenv install

** how to run
      For the test, run following command from your bash(or cmd)
         pytest
      For the linting check, run following command
         ./run_lint_check


