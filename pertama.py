import shapefile


class Pertama:

    def __init__(self):
        self.pertama = shapefile.Writer('pertama', shapeType=shapefile.POLYGON)
        self.pertama.shapeType
        self.pertama.field('nama_ruangan', 'C')
    # Jangan keatas

    def baak(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[0, 0], [4, 0], [4, 8], [0, 8], [0, 0]]])

    def bauk(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[4, 0], [13, 0], [13, 8], [4, 8], [4, 0]]])

    # Jangan kebawah
    def close(self):
        self.pertama.close()
