"""For the exercise, you will edit two functions in this file. See the function docstrings
under 'get_cases_7day_rolling_avg' and 'test_data_freshness' for more detailed instructions.
"""

import database_loader


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

    raise NotImplementedError("Delete this line once you've implemented a solution")


def test_data_freshness(db_connection):
    """On any given day we expect that yesterday's data should be available.
       Write a test that asserts that yesterday's data is available in the
       covid_cases table.

    Parameters:
    - db_connection: a sqlite database connection
    """

    raise NotImplementedError("Delete this line once you've implemented a solution")


if __name__ == "__main__":
    main()
