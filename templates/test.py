import os
import logging
from cgi import logfp
from multiprocessing.util import log_to_stderr

def show_strings(string_value):
    global logs
    match string_value:
        case "num":
            print(string_value)
            logs = string_value
            return logs
        case "string":
            print(string_value)
            return f"string entered: {logs}"
        case "":
            print(string_value)
            return logs
        
import csv

def show_sql_string_from_csv(csv_file_path):
    sql_string = ""
    character_lesson_id = 2693 

    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            user_id = row['user_id']
            character_uid = row['character_uid']
            
            sql_string += f'''
insert into user_character_lesson 
(character_lesson_id, user_id, character_uid, 
`rank`, exp, stat_type1, stat_type2, stat_type3, 
stat_value1, stat_value2, stat_value3, latest_lesson_date, 
create_date, update_date) 
values ({character_lesson_id}, {user_id}, {character_uid}, @rank, 
@exp, @stat_type1, @stat_type2, @stat_type3, @stat_value1, 
@stat_value2, @stat_value3, @latest_lesson_date, @create_date, @update_date);
'''
            character_lesson_id += 1  

    return sql_string


csv_file_path = 'character.csv'
print("STATSH!")

sql_result = show_sql_string_from_csv(csv_file_path)

file_path = 'output.txt'
with open(file_path, 'w') as file:
    file.write(sql_result)
print("TEST COMMIT~~!!2!!")

print(f"SQL 쿼리가 {file_path}에 저장되었습니다.")



