
class Dokter:
    def __init__(self, **kwargs):
        self.id_dokter = kwargs.get("id dokter")
        self.nama = kwargs.get("nama")
        self.nomor_pegawai = kwargs.get("nomor pegawai")
    
    def __str__(self):
        return (
            f'ID Dokter: {self.id_dokter}'
            f'Nama: {self.nama}'
            f'Nomor Pegawai: {self.nomor_pegawai}'
        )
    
class DokterUmum(Dokter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tarif = kwargs.get("tarif")
        self.tanggal_bertugas = kwargs.get("tanggal")

        self.penanganan = None
    
    def __str__(self):
        return (
            f'ID Dokter: {self.id_dokter}'
            f'Nama: {self.nama}'
            f'Nomor Pegawai: {self.nomor_pegawai}'
            f'Tarif: {self.tarif}'
            f'Hewan Ditangani: {self.penanganan}'
            f'Tanggal Bertugas: {self.tanggal_bertugas}'
        )
    
    def assignPet(self, id_hewan):
        self.penanganan = id_hewan
        print(f'Berhasil menugaskan {self.nama} untuk menangani hewan {id_hewan}')

class DokterSpesialis(Dokter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tarif = kwargs.get("tarif")
        self.tanggal_bertugas = kwargs.get("tanggal")
        self.spesialisasi = kwargs.get("spesialisasi")

        self.penanganan = None
    
    def __str__(self):
        return (
            f'ID Dokter: {self.id_dokter}'
            f'Nama: {self.nama}'
            f'Nomor Pegawai: {self.nomor_pegawai}'
            f'Tarif: {self.tarif}'
            f'Hewan Ditangani: {self.penanganan}'
            f'Tanggal Bertugas: {self.tanggal_bertugas}'
            f'Spesialisasi: {self.spesialisasi}'
        )
    
    def assignPet(self, id_hewan):
        self.penanganan = id_hewan
        print(f'Berhasil menugaskan {self.nama} untuk menangani hewan {id_hewan}')