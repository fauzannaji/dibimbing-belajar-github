import csv

def read_csv(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    read_csv('data.csv')
