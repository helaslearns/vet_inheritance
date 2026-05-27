from __future__ import annotations

from Hewan.Hewan import Hewan, Kucing, Anjing

_dataDokter = []

class Dokter:
    _counter = 0
    def __init__(self, nama: str, nomor_pegawai:str):
        self.nama = nama
        self.nomor_pegawai = nomor_pegawai
        self.id_dokter = f'DR{Dokter._counter:02d}' # Auto generate ID untuk dokter
        self.penanganan = [None]
        Dokter._counter += 1

        _dataDokter.append(self.nama)

    def assignPet(self, hewan: Hewan):
        if isinstance(hewan, Hewan | Kucing | Anjing):
            print(f'dr. {self.nama} ({self.id_dokter}) telah ditugaskan untuk merawat {hewan.id_hewan}')
    
    def unassignPet(self, hewan: Hewan):
        if self.penanganan is None:
            print(f'dr. {self.nama} ({self.id_dokter}) sedang tidak menangani hewan peliharaan!')
        else:
            print(f'dr. {self.nama} ({self.id_dokter}) telah menyelesaikan penanganan untuk {hewan.id_hewan}')

    def __str__(self):
        return(
            f'Nama Dokter: {self.nama}\n'
            f'Nomor Pegawai: {self.nomor_pegawai}'
        )
    
class DokterUmum(Dokter):
    def __init__(self, nama: str, nomor_pegawai:str, tarif: int):
        super().__init__(nama, nomor_pegawai)
        self.tarif = tarif
    
    def assignPet(self, hewan: Hewan):
        super().assignPet(hewan)

    def unassignPet(self, hewan: Hewan):
        super().unassignPet(hewan)

    def __str__(self):
        return(
            super().__str__() + f'\nTarif: {self.tarif}'
        )

class DokterSpesialis(Dokter):
    def __init__(self, nama: str, nomor_pegawai:str, spesialisasi: str, tarif: int):
        super().__init__(nama, nomor_pegawai)
        self.spesialisasi = spesialisasi
        self.tarif = tarif

    def __str__(self):
        return(
            super().__str__() + f'\nSpesialisasi: {self.spesialisasi}\nTarif: {self.tarif}'
        )