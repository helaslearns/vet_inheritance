class Hewan:
    def __init__(self, **kwargs):
        self.id_hewan = kwargs.get("id hewan")
        self.nama = kwargs.get("nama")
        self.usia = kwargs.get("usia")
        self.berat = kwargs.get("berat")
        self.id_pemilik = kwargs.get("id pemilik")
    
    def __str__(self):
        return (
            f'ID Hewan: {self.id_hewan}'
            f'Nama: {self.nama}'
            f'Usia: {self.usia} tahun'
            f'Berat: {self.berat} kg'
            f'ID Pemilik: {self.id_pemilik}'
        )

class Kucing(Hewan):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jenis_bulu = kwargs.get("jenis bulu")
    
    def __str__(self):
        return (
            f'ID Hewan: {self.id_hewan}'
            f'Nama: {self.nama}'
            f'Usia: {self.usia} tahun'
            f'Berat: {self.berat} kg'
            f'ID Pemilik: {self.id_pemilik}'
            f'Jenis Bulu: {self.jenis_bulu}'
        )
    
class Anjing(Hewan):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jenis_ras = kwargs.get("jenis ras")
    
    def __str__(self):
        return (
            f'ID Hewan: {self.id_hewan}'
            f'Nama: {self.nama}'
            f'Usia: {self.usia} tahun'
            f'Berat: {self.berat} kg'
            f'ID Pemilik: {self.id_pemilik}'
            f'Jenis Ras: {self.jenis_ras}'
        )