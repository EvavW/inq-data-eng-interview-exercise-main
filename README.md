## Setup
The Pandas library has been added as a dependency to this project to allow for easier debugging of query results
as well as for a new printed version of the database table.
Follow the below instructions to set up a virtual enviroment and install dependecies

1. Create a virtual environment at the top level of the project. Make sure your version of Python is updated to at least version 3.6. This directory will not be tracked in git, see the `.gitignore` file to change this:
   .. code-block:: bash

      python -m venv ./

2. Activate the virtual environment:
 .. code-block:: bash

      source ./venv/bin/activate

3. Install dependencies:
 .. code-block:: bash

    pip install -r requirements.txt



# Inquirer Data Engineering Candidate Exercise
In this exercise, you'll edit the `__main__.py` file to write some queries and tests against a database with historical COVID-19 case data. 

## Execution and Requirements
You can run the exercise with the following command:
```shell
python __main__.py
```

The execise does not require any external dependencies, and should run on Python
3.6 or greater.

## Contents
This exercise contains two files: 
### `__main__.py`
You will be editing two functions in `__main__.py`:
- `get_cases_7day_rolling_avg`
- `test_data_freshness`

See the docstrings under these two functions for more detailed instructions.

### `database_loader.py`
The main function in this module is named `load_database`, which performs the
following steps:
1. Creates a sqlite database, and a table named `covid_cases` in that database.
2. Loads the table `covid_cases` with U.S. state-level data on COVID-19 cases from the [New York Times](https://github.com/nytimes/covid-19-data).
3. Performs a data validation check against the data in `covid_cases`

## Data Dictionary
### `covid_cases` 
- `date` (text): The reported date for the data (in `YYYY-MM-DD` format).
- `state` (text): The name of the U.S. state, district, or territory.
- `cases` (integer): The number of new cases of Covid-19 reported that day, including both confirmed and probable.
- `deaths` (integer): The total number of new deaths from Covid-19 reported that day, including both confirmed and probable.

Note that, due to sqlite limitations, the columne `date` has data type `text`; however,
the data validation step checks that `date` only contains properly-formatted values.
