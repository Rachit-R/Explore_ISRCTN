import sqlite3
import pandas as pd

def execute_and_save_query(conn, query, filename):
    """
    Execute  given SQL query and save the result to a CSV file.

    Parameters:
    - conn: SQLite database connection object.
    - query: SQL query to execute.
    - filename: Path to the CSV file to save the results.
    """
    df = pd.read_sql_query(query, conn)
    df.to_csv(filename, index=False)

def study_initiations_over_years_query(conn):
    query = """
    SELECT 
        strftime('%Y', Overall_study_start_date) AS Study_year,
        COUNT(*) AS StudyCount
    FROM ISRCTN 
    GROUP BY Study_year 
    ORDER BY Study_year;
    """
    execute_and_save_query(conn, query, 'csv/study_initiations_over_years.csv')

def studies_by_age_group_query(conn):
    query = """
    SELECT 
        Age_group, 
        COUNT(*) AS StudyCount 
    FROM ISRCTN 
    GROUP BY Age_group 
    ORDER BY StudyCount DESC;
    """
    execute_and_save_query(conn, query, 'csv/studies_by_age_group.csv')

def studies_by_participant_type_query(conn):
    query = """
    SELECT 
        Participant_types, 
        COUNT(*) AS StudyCount 
    FROM ISRCTN 
    GROUP BY Participant_types 
    ORDER BY StudyCount DESC;
    """
    execute_and_save_query(conn, query, 'csv/studies_by_participant_type.csv')

def studies_by_study_setting_query(conn):
    query = """
    SELECT 
        Study_settings AS Study_setting, 
        COUNT(*) AS StudyCount 
    FROM ISRCTN 
    GROUP BY Study_setting 
    ORDER BY StudyCount DESC;
    """
    execute_and_save_query(conn, query, 'csv/studies_by_study_setting.csv')

def studies_and_avg_target_participants_by_year_query(conn):
    query = """
    SELECT 
        strftime('%Y', Overall_study_start_date) AS Study_year,
        COUNT(*) AS StudyCount,
        CAST(AVG(Target_number_of_participants)AS INT) AS Average_target_participants
    FROM ISRCTN 
    GROUP BY Study_year 
    ORDER BY Study_year;
    """
    execute_and_save_query(conn, query, 'csv/studies_and_avg_target_participants_by_year.csv')

def studies_by_condition_category_query(conn):
    query = """
    SELECT 
        Condition_category, 
        COUNT(*) AS StudyCount 
    FROM ISRCTN
    GROUP BY Condition_category
    ORDER BY StudyCount DESC;
    """
    execute_and_save_query(conn, query, 'csv/studies_by_condition_category.csv')

def studies_by_study_design_query(conn):
    query = """
    SELECT 
        Primary_study_design,
        COUNT(*) AS StudyCount
    FROM ISRCTN
    GROUP BY Primary_study_design
    ORDER BY StudyCount DESC;
    """
    execute_and_save_query(conn, query, 'csv/studies_by_study_design.csv')

# Main function to run all queries
def run_all_queries(conn):
    study_initiations_over_years_query(conn)
    studies_by_age_group_query(conn)
    studies_by_participant_type_query(conn)
    studies_by_study_setting_query(conn)
    studies_and_avg_target_participants_by_year_query(conn)
    studies_by_condition_category_query(conn)
    studies_by_study_design_query(conn)

