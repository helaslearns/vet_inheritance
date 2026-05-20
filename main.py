from Dokter import Dokter
from Pemilik import Pemilik
from Hewan import Hewan

def main():
    dokter1 = Dokter(
        id_dokter="D001",
        nama="Dr. Andi",
        nomor_pegawai="12345"
    )
    print(dokter1)

    pemilik1 = Pemilik(
        id_pemilik="P001",
        nama="Budi",
        nomor_telepon="08123456789"
    )
    print(pemilik1)

    hewan1 = Hewan(
        id_hewan="H001",
        nama="Kucing Lucu",
        usia=2,
        berat=4,
        id_pemilik="P001"
    )
    print(hewan1)

if __name__ == "__main__":
    main()
