## Showcase SQL skills
1. Create Data Pipelines from Raw Data
   1. Apple Jobs
      1. [Data](https://www.kaggle.com/datasets/aesophor/raw-data)
      2. Suppose this dataset is a live table that stores all of Apple’s job listings, 
      but your manager only needs a table that shows all of the distinct skills mentioned, 
      as well as a count of each skill mentioned segmented by state.
2. Kickstarter Projects
   1. [Data](https://www.kaggle.com/datasets/kemical/kickstarter-projects)
   2. See if you can manipulate the table using SQL so that it shows the number of projects per category, 
   the average goal amount per category, the average amount pledged per category, 
   the percentage of projects that met their goal by category, and the average time from launch to deadline by category.
3. SQL Coding Questions 
   1. Leetcode
4. SQL Case Studies in mode  
   [Mode’s SQL editor](https://mode.com/sql-tutorial/intro-to-intermediate-sql/)
   1. [Investigating a Drop in User Engagement](https://mode.com/sql-tutorial/a-drop-in-user-engagement/)
      1. [info](https://mode.com/sql-tutorial/sql-business-analytics-training/)
      2. [guidence](https://towardsdatascience.com/sql-case-study-investigating-a-drop-in-user-engagement-510b27d0cbcc?source=friends_link&sk=49cdc679e66cae75257b955db51f4fe5)
   2. [Understanding Search Functionality](https://mode.com/sql-tutorial/understanding-search-functionality/)
   This case is more focused on product analytics. 
   Here, you’ll be required to dive into the data and determine whether the user experience is good or bad. 
   What makes this case interesting is that it’s up to you to determine what ‘good’ and ‘bad’ means 
   and how the user experience will be evaluated.
   3. [Validating A/B Test Results](https://mode.com/sql-tutorial/validating-ab-test-results/)
   One of the most practical data science applications is performing A/B tests. 
   In this case study, you’ll dive into the results of an A/B test where there was a 50% difference between the control and treatment groups. 
   Your task for this case is to validate or invalidate the results after a thorough analysis.

## SQL notes
### Date related
EXTRACT  
DATE_TRUNC

### Window Function
- Running total  
"Take the sum of *duration_seconds* over the entire result set, in order by *start_time*."
   ```sql
   SELECT duration_seconds,
         SUM(duration_seconds) OVER (ORDER BY start_time) AS running_total
   FROM tutorial.dc_bikeshare_q1_2012
   ```


- To narrow the window from the entire dataset to individual groups within the dataset, by `PARTITION BY`.
   ```sql
   SELECT start_terminal,
         duration_seconds,
         SUM(duration_seconds) OVER
            (PARTITION BY start_terminal ORDER BY start_time)
            AS running_total
   FROM tutorial.dc_bikeshare_q1_2012
   WHERE start_time < '2012-01-08'
   ```

- Show a running total of the duration of bike rides, grouped by end_terminal, and with ride duration sorted in descending order.
   ```sql
   SELECT end_terminal,
       duration_seconds,
       SUM(duration_seconds) OVER
         (PARTITION BY end_terminal ORDER BY duration_seconds DESC)
         AS running_total
   FROM tutorial.dc_bikeshare_q1_2012
   WHERE start_time < '2012-01-08'
   ```

- `ROW_NUMBER()`
   ```sql
   SELECT start_terminal,
       start_time,
       duration_seconds,
       ROW_NUMBER() OVER (PARTITION BY start_terminal
                          ORDER BY start_time)
                    AS row_number
   FROM tutorial.dc_bikeshare_q1_2012
   WHERE start_time < '2012-01-08'
   ```

- `RANK()`  
(If at some terminals have rides with two identical start times, `ROW_NUMBER()` gives different numbers, while `RANK()` would give the same number)
   ```sql
   SELECT start_terminal,
       duration_seconds,
       RANK() OVER (PARTITION BY start_terminal
                    ORDER BY start_time)
              AS rank
   FROM tutorial.dc_bikeshare_q1_2012
   WHERE start_time < '2012-01-08'
   ```

- `DENSE_RANK()`: compared to `RANK()`, no ranks would be skipped.
e.g. 
   - `RANK()`: 1, 2, 2, 2, 5
   - `DENSE_RANK()`: 1, 2, 2, 2, 3

- `NTILE(n)`
   - `NTILE(100)` -> percentile

- `LAG(colname, num_rows_away)` (pulls from previous rows) 
and `LEAD(colname, num_rows_away)` (pulls from following rows) 

- Defining a window alias using `WINDOW` (after `WHERE`)
Original:
```sql
SELECT start_terminal,
       duration_seconds,
       NTILE(4) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
         AS quartile,
       NTILE(5) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
         AS quintile,
       NTILE(100) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
         AS percentile
   FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
 ORDER BY start_terminal, duration_seconds
 ```

 Using sindow alias:
 ```sql
SELECT start_terminal,
      duration_seconds,
      NTILE(4) OVER ntile_window AS quartile,
      NTILE(5) OVER ntile_window AS quintile,
      NTILE(100) OVER ntile_window AS percentile
  FROM tutorial.dc_bikeshare_q1_2012
WHERE start_time < '2012-01-08'
WINDOW ntile_window AS (PARTITION BY start_terminal ORDER BY duration_seconds)
 ```