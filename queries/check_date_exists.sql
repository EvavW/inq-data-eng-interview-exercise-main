/*Return the number of rows in covid_cases where date matches the argument. There is no quarantee that the max date in covid_case will be "yesterday's" date, so this will test for the existence of any given date*/


SELECT count(*) as rows_at_date
FROM   covid_cases
WHERE  date == "{date}";
