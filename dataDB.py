import csv

def generarBD():
    DB=[]
    with open("./data.csv",encoding="latin") as csvfile:
        csv_reader = csv.reader(csvfile,delimiter=",")
        line = 0
        for row in csv_reader:
            if line == 0:
                line=1
                continue
            aux = [str(x) for x in row]
            DB.append(aux)
    
    return DB

if __name__ == "__main__":
    print(generarBD())