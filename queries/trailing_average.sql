SELECT *,
       avg(cases) OVER(PARTITION BY state
                       ORDER BY state, date rows between 6 preceding and current row) as trailing_avg
FROM   (SELECT state,
               date,
               cases
        FROM   covid_cases
        GROUP BY state, date);
