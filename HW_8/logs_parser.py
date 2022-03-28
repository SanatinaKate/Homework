import argparse
import json
import os
import re


DEFAULT_PATH = "Homework_08/logs/access.log"
METHODS = ("GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "CONNECT", "OPTIONS", "TRACE")


def top3_modify(top3_list, sort_key, current, unique_key=None):
    length = len(top3_list)
    found = False
    sort = False
    if unique_key is not None:
        i = -1
        while (not found) and (i < length - 1):
            i += 1
            found = (top3_list[i][unique_key] == current[unique_key])
        if found and (current[sort_key] > top3_list[i][sort_key]):
            top3_list[i] = current
            sort = (i > 0)
    if not found:
        if length < 3:
            top3_list.append(current)
            sort = (length > 0)
        elif current[sort_key] > top3_list[2][sort_key]:
            top3_list[2] = current
            sort = True
    if sort:
        top3_list = sorted(top3_list, key=lambda x: x[sort_key], reverse=True)
    return top3_list


parser = argparse.ArgumentParser()
parser.add_argument("-p", action="store", dest="path", default=DEFAULT_PATH, help="Path to log-files")
args = parser.parse_args()
logs_path = args.path
logs = []
if os.path.isdir(logs_path):
    if logs_path[-1] != "/":
        logs_path += "/"
    for file in os.listdir(logs_path):
        if os.path.isfile(logs_path + file) and file.endswith(".log"):
            logs.append(logs_path + file)
elif os.path.isfile(logs_path) and logs_path.endswith(".log"):
    logs.append(logs_path)
if len(logs) > 0:
    for log in logs:
        print(f"Statistics for file {log}:")
        with open(log, "r") as log_file:
            results = {"HTTP REQUESTS": 0}
            for method in METHODS:
                results[method] = 0
            req_by_ip = {}
            top3_ip = []
            top3_req = []
            for line in log_file:
                ip = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", line).group()
                date_time = re.search(r"\d{1,2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4}", line).group()
                date_time = date_time[:11] + " " + date_time[12:]
                search = re.search(r"] \"(\w+) ", line)
                if search is not None:
                    method = search.group(1)
                    if method not in METHODS:
                        method = "UNKNOWN"
                else:
                    method = "UNKNOWN"
                duration = int(re.search(r"\d+$", line).group())
                search = re.search(r"http(s?)://[\w\-./?=&]+", line)
                url = search.group() if search is not None else "-"
                results["HTTP REQUESTS"] += 1
                results[method] = results[method] + 1 if method in results.keys() else 1
                req_by_ip[ip] = req_by_ip[ip] + 1 if ip in req_by_ip.keys() else 1
                data = {"IP ADDRESS": ip, "SENT REQUESTS": req_by_ip[ip]}
                top3_ip = top3_modify(top3_ip, sort_key="SENT REQUESTS", current=data, unique_key="IP ADDRESS")
                data = {"METHOD": method, "URL": url, "IP ADDRESS": ip, "DURATION": duration, "DATE & TIME": date_time}
                top3_req = top3_modify(top3_req, sort_key="DURATION", current=data)
        results["TOP-3 IP ADDRESSES BY SENT REQUESTS"] = top3_ip
        results["TOP-3 REQUESTS BY DURATION"] = top3_req
        with open(f"{log}.json", "w") as json_file:
            json.dump(results, json_file, indent=4)
            json_file.write("\n")
        print(json.dumps(results, indent=4))
        print(f"Statistics is also saved into file {log}.json\n")
else:
    print("Given path is incorrect or does not contain any log-files")
