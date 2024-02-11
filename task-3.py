import sys
from collections import defaultdict
import re
from colorama import Fore, Style
def parse_log_line(line: str) -> dict:
    date, time, level, *message = line.split(' ')
    if not re.match(r"\d{4}\-\d{2}-\d{2}", date):
        print(Fore.RED + f"Неправильний формат дати у рядку '{line.strip()}'." + Style.RESET_ALL)
        return None
    if not re.match(r"\d{2}\:\d{2}:\d{2}", time):
        print(Fore.RED + f"Неправильний формат часу у рядку '{line.strip()}'." + Style.RESET_ALL)
        return None
    return {'date':date, 'time':time, 'level':level, 'message':' '.join(message)}

def load_logs(file_path: str) -> list:
    with open(file_path,"r+") as lf:
        lines = list(filter(lambda x: x is not None,(map(parse_log_line,lf.readlines()))))
    return lines

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x: x['level'] == level, logs))

def count_logs_by_level(logs: list) -> dict:
    count_dict = defaultdict()
    count_dict.default_factory = int
    for log in logs:
        count_dict[log['level']] += 1
    return dict(count_dict)    
    
def display_log_counts(counts: dict):
    print(f"{'Рівень логування':20} | Кількість")
    print(f"{'-'*20} | {'-'*10}")
    print("\n".join(list(map(lambda x: f"{x:20} | {counts[x]}",counts))))

if __name__=="__main__":
    filename = sys.argv[1]
    logs = load_logs(file_path = filename)
    display_log_counts(count_logs_by_level(logs))
    if len(sys.argv) == 3 :
        level = sys.argv[2]
        logs = filter_logs_by_level(logs,level)
        print()
        print(f"Деталі логів для рівня '{level}': ")
        print(''.join(map(lambda x: f"{x['date']} {x['time']} - {x['message']}" ,logs)))