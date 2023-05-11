import datetime
import tensorflow as tf
import os

def get_a_unique_id(now) -> int:
    if now == None:
        now = datetime.now()
    now_id = int(now.strftime('%Y%m%d%H%M%S'))
    return now_id

def get_todays_date_in_str(now) -> str:
    if now == None:
        now = datetime.now()
    date_in_yyyy_mm_dd = now.strftime('%Y%m%d')
    return date_in_yyyy_mm_dd

def load_model(file_path):
    if os.path.exists(file_path):
        return tf.keras.models.load_model(file_path)
    else:
        print("File does not exist in the directory.")
    


