from __future__ import annotations

class Hewan:
    _counter = 1  

    def __init__(self, **kwargs):
        self.id_hewan = f"H{Hewan._counter:03d}"  
        Hewan._counter += 1

        self.nama = kwargs.get("nama")
        self.usia = kwargs.get("usia")
        self.berat = kwargs.get("berat")
        self.id_pemilik = kwargs.get("id_pemilik")  
    
    def __str__(self):
        return (
            f'ID Hewan: {self.id_hewan}\n'
            f'Nama: {self.nama}\n'
            f'Usia: {self.usia} tahun\n'
            f'Berat: {self.berat} kg\n'
            f'ID Pemilik: {self.id_pemilik}'
        )

class Kucing(Hewan):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jenis_bulu = kwargs.get("jenis_bulu")
    
    def __str__(self):
        return super().__str__() + f'\nJenis Bulu: {self.jenis_bulu}'
    
class Anjing(Hewan):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jenis_ras = kwargs.get("jenis_ras")
    
    def __str__(self):
        return super().__str__() + f'\nJenis Ras: {self.jenis_ras}'