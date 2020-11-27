import csv


def save_result(data, columns, path, result):
    csv_file = open(path + result + ".csv", "w", encoding="UTF-8")
    csv_file_writer = csv.writer(csv_file)

    # Header
    csv_file_writer.writerow([columns[0], columns[1], columns[2]])

    count = 0
    for key, val in data.items():
        count += 1
        csv_file_writer.writerow([str(count), key, str(val)])


def save_stats(experiments, total, average, columns, path, name):
    csv_file = open(path + name + ".csv", "w", encoding="UTF-8")
    csv_file_writer = csv.writer(csv_file)

    # Header
    csv_file_writer.writerow([columns[0], columns[1], columns[2]])

    # Stats
    csv_file_writer.writerow([experiments, total, average])
