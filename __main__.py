"""For the exercise, you will edit two functions in this file. See the function docstrings
under 'get_cases_7day_rolling_avg' and 'test_data_freshness' for more detailed instructions.
"""
import pandas as pd

from datetime import date, timedelta

from exc import FreshnessError
import database_loader

SQL_DIR = "queries"
TRAILING_AVG_QUERY = "trailing_average.sql"
CHECK_DATE_QUERY = "check_date_exists.sql"


def main():
    """Main entry point for the script"""
    cxn = database_loader.get_db_connection()
    database_loader.load_database(cxn)
    print(get_cases_7day_rolling_avg(cxn))
    test_data_freshness(cxn)


def get_cases_7day_rolling_avg(db_connection):
    """Write a query that returns, the average number of new cases reported
       over the previous seven days of data for each day and state. In other
       words, the seven-day trailing average.

    Parameters:
    - db_connection: a sqlite database connection
    """
    # load query
    query = _load_query(TRAILING_AVG_QUERY)

    # execute query, return result
    # use pandas to get a dataframe of the table that prints nicely
    result = pd.read_sql_query(query, db_connection)

    return result


def test_data_freshness(db_connection):
    """On any given day we expect that yesterday's data should be available.
       Write a test that asserts that yesterday's data is available in the
       covid_cases table.

    Parameters:
    - db_connection: a sqlite database connection
    """
    # crete cursor
    cursor = db_connection.cursor()

    # get yesterday's date as string formatted like YYYY-MM-DD
    today = date.today()
    yesterday = today - timedelta(days=1)
    yesterday = str(yesterday)

    # create query with yesterday's date as an argument
    query = _load_query(CHECK_DATE_QUERY, date=(yesterday))

    # execute query, test result
    result = pd.read_sql_query(query, db_connection)

    if result.iloc[0, 0] == 0:
        raise FreshnessError(
            f"covid_cases does not contain rows from yesterday ({yesterday})"
        )


def _load_query(file_str, **kwargs):
    """
    Load SQL query from file, reuturn as text.

    Parameters:
    - file_str: name of the file (should end with .sql)
    - kwargs: any variables needed for string formatting

    """
    with open("/".join([SQL_DIR, file_str]), "r") as sql_file:
        query = sql_file.read().format(**kwargs)

    return query


if __name__ == "__main__":
    main()
