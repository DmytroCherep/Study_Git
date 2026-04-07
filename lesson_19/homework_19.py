import logging
from datetime import datetime

KEY = "TSTFEED0300|7E3E|0400"


logging.basicConfig(
    filename="hb_test.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


def extract_time(line):
    idx = line.find("Timestamp ")
    if idx == -1:
        return None

    time_str = line[idx + 10: idx + 18]
    return datetime.strptime(time_str, "%H:%M:%S")


def process_log(file_path):
    filtered = []

    # 1️⃣ фільтр по ключу
    with open(file_path, "r") as f:
        for line in f:
            if KEY in line:
                filtered.append(line)

    # 2️⃣ витяг часу
    times = []
    for line in filtered:
        t = extract_time(line)
        if t:
            times.append(t)

    # 3️⃣ аналіз
    for i in range(len(times) - 1):
        t1 = times[i]
        t2 = times[i + 1]

        diff = abs((t1 - t2).total_seconds())

        if 31 < diff < 33:
            logging.warning(f"{t2.time()} - heartbeat {diff} sec")

        elif diff >= 33:
            logging.error(f"{t2.time()} - heartbeat {diff} sec")


if __name__ == "__main__":
    process_log("hblog.txt")