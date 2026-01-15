import csv
with open('visit_log.csv', 'r', encoding='utf-8') as visits, \
     open('funnel.csv', 'w', newline='', encoding='utf-8') as output:
    reader = csv.reader(visits)
    writer = csv.writer(output)
    header = next(reader)
    writer.writerow(header)
    for row in reader:
        if len(row) >= 3 and row[2].strip():
            writer.writerow(row)
print("Первые три строки файла funnel.csv:")
print("-" * 25)
with open('funnel.csv', 'r', encoding='utf-8') as f:
    lines_printed = 0
    for line in f:
        print(line.strip())
        lines_printed += 1
        if lines_printed >= 3:
            break