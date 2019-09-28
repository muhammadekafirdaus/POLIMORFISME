class FakultasTeknik:
    def __init__(self,Universitas, Fakultas, TahunAjar):
        self.univ = Universitas
        self.fak = Fakultas
        self.TA = TahunAjar
    def CetakData(self):
        print('Universitas   : ',self.univ)
        print('Fakultas      : ',self.fak)
        print('Tahun Ajaran  : ',self.TA)

class TeknikKomputer(FakultasTeknik):
    def __init__(self,Universitas, Fakultas, TahunAjar, JumlahAngkatan):
        self.JA = JumlahAngkatan
        FakultasTeknik.__init__(self,Universitas, Fakultas, TahunAjar)
    def CetakData(self):
        
        print('Teknik Komputer')
        print('Universitas   : ', self.univ)
        print('Fakultas      : ', self.fak)
        print('Tahun Ajaran  : ', self.TA)
        print('Jumlah Angkatan di prodi Teknik Komputer adalah :', self.JA)
        

class PTIK(FakultasTeknik):
    def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan, Jurusan):
        self.JA = JumlahAngkatan
        self.J = Jurusan
        FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)

    def CetakData(self):
        print('PTIK')
        print('Universitas   : ', self.univ)
        print('Fakultas      : ', self.fak)
        print('Jurusan       : ', self.J)
        print('Tahun Ajaran  : ', self.TA)
        print('Jumlah Angkatan di prodi Teknik PTIK adalah :', self.JA)
        
class Mekatronika(FakultasTeknik):
    def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan):
        self.JA = JumlahAngkatan
        FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)

    def CetakData(self):
        print('MEKATRONIKA')
        print('Universitas   : ', self.univ)
        print('Fakultas      : ', self.fak)
        print('Tahun Ajaran  : ', self.TA)
        print('Jumlah Angkatan di prodi Teknik MEKATRONIKA adalah :', self.JA)
        

def main():

    a = FakultasTeknik('UNM', 'Teknik', 2018, )
    a.CetakData()

    del a

    a = TeknikKomputer('UNM', 'Teknik', 2018, 2 )
    a.CetakData()

    b = PTIK('UNM', 'Teknik', 2018, 15, 'Pendidikan Teknik INFORMATIKA')
    b.CetakData()

    del b

    b = Mekatronika('UNM', 'Teknik', 2018, 12)
    b.CetakData()



if __name__ == "__main__":
    main()