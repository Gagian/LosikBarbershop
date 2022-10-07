from django.db import models

# Create your models here.
class pelayan(models.Model):
    idpelayan = models.AutoField(primary_key=True)
    namapelayan = models.CharField(max_length=50)
    notelp = models.IntegerField()
    alamat = models.CharField(max_length=50)

    def __str__(self):
        return str(self.namapelayan)

class layanan(models.Model):
    idlayanan = models.AutoField(primary_key=True)
    jenislayanan = models.CharField(max_length=15)
    hargalayanan = models.IntegerField()

    def __str__(self):
        return str(self.jenislayanan)

class transaksi(models.Model):
    idtransaksi = models.AutoField(primary_key=True)
    idpelayan = models.ForeignKey(pelayan,on_delete=models.CASCADE)
    namapelanggan = models.CharField(max_length=50)
    tanggaltransaksi = models.DateField()

    def __str__(self):
        return str(self.namapelanggan)

class detaillayanan(models.Model):
    iddetaillayanan = models.AutoField(primary_key=True)
    idtransaksi = models.ForeignKey(transaksi,on_delete=models.CASCADE)
    idlayanan = models.ForeignKey(layanan,on_delete=models.CASCADE)

    
