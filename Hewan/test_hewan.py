import Hewan 

def main():
    hewan1 = Hewan.Hewan(nama="Kucing", usia=2, berat=3.5, id_pemilik="P001")
    print(hewan1)

    hewan2 = Hewan.Kucing(nama="Mimi", usia=3, berat=4.0, id_pemilik="P002", jenis_bulu="Panjang")
    print(hewan2)

    hewan3 = Hewan.Anjing(nama="Buddy", usia=1, berat=10.0, id_pemilik="P003", jenis_ras="Golden Retriever")
    print(hewan3)

if __name__ == "__main__":
    main()