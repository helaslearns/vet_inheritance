class Pemilik:
    def __init__(self, **kwargs):
        self.id_pemilik = kwargs.get("id pemilik")
        self.nama = kwargs.get("nama")
        self.nomor_telepon = kwargs.get("nomor telepon")
    
    def __str__(self):
        return (
            f'ID Pemilik: {self.id_pemilik}'
            f'Nama: {self.nama}'
            f'Nomor Telepon: {self.nomor_telepon}'
        )