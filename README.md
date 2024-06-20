# Exploring ISRCTN data 

Exploring ISRCTN data which consisted of completed clinical trails.


The Explore_ISRCTN project entailed downloading a CSV file of clinical trials data, cleaning and transforming it using Python and Pandas, and loading it into an SQLite database. 
Altered table within database to refine certain fields for better grouping. 
Various SQL queries were executed to analyse the data, and the results were saved as CSV files. 
These CSV files were then used to create interactive visualizations in Tableau. The process of running multiple queries at once was automated and modularised

The final analysis is visualised using Tableau dashboard.
[Exploring_Completed_Trials_ISRCTN](https://public.tableau.com/views/Exploring_Completed_Trials_ISRCTN/Dashboard1?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link)

## Project Structure
- clean_and_load.py: Reads the CSV file, cleans the column names (removing parentheses and replacing spaces with underscores), and loads the cleaned data into an SQLite database.
- main.py: Connects to the SQLite database, runs all the predefined queries, and saves the results to CSV files
- queries.py: Contains the SQL queries and functions to execute each query, saving the results to CSV files.
- SQL_DB_ALTERATIONS.sql: Contains all the alterations I made to the database after loading in the cleaned CSV. Through use of UPDATE to update or modify the value of a column in the table.The purpose was to better define categories.

### Processes
Data Cleaning and Transformation
 - Pandas: Utilised for reading, cleaning, and transforming CSV data.
 - Data Cleaning: Removed unwanted characters from column names

Database Management & Analysis
- SQL: storing data, queries for data analysis and UPDATE data.
    
Automation
- Python Scripting: Automated data cleaning, loading, and querying processes.

Data Visualization
- Tableau: Created interactive visualizations to present analysis results.

Version Control
- Git: Employed for version tracking and project management.

 Queries Included

    Study Initiations Over Years
    Studies by Age Group
    Studies by Participant Type
    Studies by Study Setting
    Studies and Average Target Participants by Year
    Studies by Condition Category
    Studies by Study Design
