
def ambil_label(file):
    # mengambil header dari file csv sebagai label
    line = file.readline()
    label = line.split(",")
    label = label[1:]
    label[-1] = label[-1][0]
    return label


def csvToArr(file):
    # mengubah matrix dalam file Csv menjadi array 2D
    arr = list()

    for x in file:
        row = x.split(",")
        row = list(map(int, row[1:]))
        arr.append(row)

    return arr

def buatDictionary(file):#mengubah list kedalam bentuk dictionary (menabaikan jarak tiap node)
    label = ambil_label(file)
    table = csvToArr(file)

    graph = dict()

    for x in range(len(table)):
        relation = list()
        for i in range(len(table[x])):
            if table[x][i]:
                relation.append(label[i])
        graph.update({label[x]: relation})
    return graph


def greedy(Graf):
    color = dict()
    for node in Graf:
        warnaTerpakai = [color[con] for con in Graf[node] if con in color]
        color[node] = warnatTersedia(warnaTerpakai)
    return color

def warnatTersedia(warna):
    Wset = set(warna)
    count = 0
    while True:
        if count not in Wset:
            return count
        count += 1


if __name__ == "__main__":
    file = open("./book1.csv")
    warna = ["merah", "hijau", 'biru', "putih"]
    graph = buatDictionary(file)
    out =greedy(graph)
    print('node \t |warna')
    for x in out:
        print(x,"\t \t", warna[out[x]])


# author : Andika Eka
#  https://github.com/andika-eka
