import datetime

def get_a_unique_id() -> int:
    now = datetime.now()
    now_id = int(now.strftime('%Y%m%d%H%M%S'))
    return now_id

def get_todays_date_in_str() -> str:
    now = datetime.now()
    date_in_yyyy_mm_dd = now.strftime('%Y%m%d')
    return date_in_yyyy_mm_dd