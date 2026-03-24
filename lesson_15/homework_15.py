import csv
import json
import logging
import os
import xml.etree.ElementTree as ET


# -------------------------
# Завдання 1 (CSV)
# -------------------------

def remove_duplicates(file1, file2, output_file):
    rows = set()

    for file in [file1, file2]:
        with open(file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.add(tuple(row))

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


# -------------------------
# Завдання 2 (JSON)
# -------------------------

def validate_json_files(folder_path, log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.ERROR,
        format='%(asctime)s - %(message)s'
    )

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            try:
                with open(file_path) as f:
                    json.load(f)
            except json.JSONDecodeError:
                logging.error(f"Invalid JSON file: {filename}")


# -------------------------
# Завдання 3 (XML)
# -------------------------

def find_in_xml(file_path, group_number):
    logging.basicConfig(level=logging.INFO)

    tree = ET.parse(file_path)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number')

        if number is not None and number.text == str(group_number):
            incoming = group.find('timingExbytes/incoming')

            if incoming is not None:
                logging.info(f"Incoming value: {incoming.text}")
                return incoming.text

    return None


# -------------------------
# Приклад виклику
# -------------------------

if __name__ == "__main__":
    # CSV
    remove_duplicates(
        "ideas_for_test/work_with_csv/file1.csv",
        "ideas_for_test/work_with_csv/file2.csv",
        "result_Cherep.csv"
    )

    # JSON
    validate_json_files(
        "ideas_for_test/work_with_json",
        "json__Cherep.log"
    )

    # XML
    find_in_xml(
        "ideas_for_test/work_with_xml/groups.xml",
        1
    )