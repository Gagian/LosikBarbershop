from multiprocessing import dummy
from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home (request):
    return render(request, 'home.html')
def pelayan (request):
    allpelayanobj = models.pelayan.objects.all()
    # getpelayanobj = models.pelayan.objects.get(idpelayan=)

    return render(request, 'pelayan.html',{
        "allpelayanobj" : allpelayanobj,
        # "getpelayanobj" : getpelayanobj,
    })

def layanan (request):
    alllayananobj = models.layanan.objects.all()
    # getlayananobj = models.layanan.objects.get(idlayanan=1)

    return render(request, 'layanan.html',{
        "alllayananobj" : alllayananobj,
        # "getlayananobj" : getlayananobj,
    })

def transaksi(request):
    alltransaksiobj = models.transaksi.objects.all()
    layananobj = models.layanan.objects.all()
    # gettransaksiobj = models.transaksi.objects.get(idtransaksi=1)
    print(alltransaksiobj,'woy')

    return render(request, 'transaksi.html',{
        "alltransaksiobj" : alltransaksiobj,
        "layananobj" : layananobj
        # "gettransaksiobj" : gettransaksiobj,
    })


def detaillayanan (request):
    alldetaillayananobj = models.detaillayanan.objects.all()
    # getdetaillayananobj = models.detaillayanan.objects.get(iddetaillayanan=1)

    return render(request, 'detaillayanan.html',{
        "alldetaillayananobj" : alldetaillayananobj,
        # "getdetaillayananobj" : getdetaillayananobj,
    })

def createdatapelayan(request):
    if request.method == 'GET':
        return render(request, 'createdatapelayan.html')
    else :
        namapelayan = request.POST['namapelayan']
        notelp = request.POST['notelp']
        alamat = request.POST['alamat']

        newpelayan = models.pelayan(
            namapelayan = namapelayan,
            notelp = notelp,
            alamat = alamat
        )
        newpelayan.save()
        return redirect('index')

def updatepelayan(request,id):
    pelayanobj = models.pelayan.objects.get(idpelayan=id)
    if request.method == "GET":
        return render(request,'updatepelayan.html',{
            'pelayan':pelayanobj,
        })
    elif request.method == 'POST':
        namapelayan = request.POST['namapelayan']
        notelp = request.POST['notelp']
        alamat = request.POST['alamat']
        pelayanobj.namapelayan = namapelayan
        pelayanobj.notelp = notelp
        pelayanobj.alamat = alamat
        pelayanobj.save()
        return redirect('index')

def deletepelayan(request,id):
    pelayanobj = models.pelayan.objects.get(idpelayan=id)
    pelayanobj.delete()
    return redirect('index')

def createdatalayanan(request):
    if request.method == 'GET':
        return render(request, 'createdatalayanan.html')
    else :
        jenislayanan = request.POST['jenislayanan']
        hargalayanan = request.POST['hargalayanan']

        newlayanan = models.layanan(
            jenislayanan = jenislayanan,
            hargalayanan = hargalayanan,
        )
        newlayanan.save()
        return redirect('layanan')

def updatelayanan(request,id):
    layananobj = models.layanan.objects.get(idlayanan=id)
    if request.method == "GET":
        return render(request,'updatelayanan.html',{
            'layanan':layananobj,
        })
    elif request.method == 'POST':
        jenislayanan = request.POST['jenislayanan']
        hargalayanan = request.POST['hargalayanan']
        layananobj.jenislayanan = jenislayanan
        layananobj.hargalayanan = hargalayanan
        layananobj.save()
        return redirect('layanan')

def deletelayanan(request,id):
    layananobj = models.layanan.objects.get(idlayanan=id)
    layananobj.delete()
    return redirect('layanan')

def createdatatransaksi(request):
    layananobj = models.layanan.objects.all()
    pelayanobj = models.pelayan.objects.all()
    if request.method == 'GET':
        return render(request, 'createdatatransaksi.html',{
            'layananobj':layananobj,
            'pelayanobj': pelayanobj
        })
    else :
        nama = request.POST['namapelanggan']
        idpelayan = request.POST['namapelayan']
        getpelayan = models.pelayan.objects.get(idpelayan = idpelayan)
        idlayanan = request.POST['jenislayanan']
        getlayanan = models.layanan.objects.get(idlayanan = idlayanan)
        tanggaltransaksi = request.POST['tanggaltransaksi']

        jumlahtransaksi = models.transaksi.objects.all().count()
        totaltrans = len(str(jumlahtransaksi))


        newtransaksi = models.transaksi(
            idpelayan = getpelayan, 
            namapelanggan = nama,
            tanggaltransaksi = tanggaltransaksi,
        )
        newtransaksi.save()
        transaksiobj = models.transaksi.objects.all().last()

        newdetaillayanan = models.detaillayanan(
            idlayanan = getlayanan, 
            idtransaksi = transaksiobj
        )
        newdetaillayanan.save()
        return redirect('transaksi')

def updatetransaksi(request,id):
    gettransaksiobj = models.transaksi.objects.get(idtransaksi=id)
    alltransaksiobj = models.transaksi.objects.all()
    alllayananobj = models.layanan.objects.all()

    if request.method == "GET":
        return render(request,'updatetransaksi.html',{
            'transaksi':alltransaksiobj,
            'layanan'  :alllayananobj,
            'gettransaksi':gettransaksiobj
        })
    else: 
        request.method == 'POST'
        idtransaksi = request.POST['idtransaksi']
        getransaksi = models.transaksi.objects.get(idtransaksi = idtransaksi)
        idlayanan = request.POST['jenislayanan']
        getlayanan = models.layanan.objects.get(idlayanan = idlayanan)

        updatetransaksi = models.detaillayanan(
            idtransaksi = getransaksi,
            idlayanan = getlayanan
        )
        updatetransaksi.save()
        return redirect('transaksi')
        # idpelayan = request.POST['idpelayan']
        # namapelanggan = request.POST['namapelanggan']
        # tanggaltransaksi = request.POST['tanggaltransaksi']
        # transaksiobj.idpelayan = idpelayan
        # transaksiobj.namapelanggan = namapelanggan
        # transaksiobj.tanggaltransaksi = tanggaltransaksi
        return redirect('layanan')

def deletetransaksi(request,id):
    transaksiobj = models.transaksi.objects.get(idtransaksi=id)
    transaksiobj.delete()
    return redirect('transaksi')

def createdatadetaillayanan(request):
    layananobj = models.layanan.objects.all()
    transaksiobj = models.transaksi.objects.all()
    if request.method == 'GET':
        return render(request, 'createdatadetaillayanan.html',{
            'layananobj': layananobj,
            'transaksiobj': transaksiobj
        })
    else :
        idtransaksi = request.POST['idtransaksi']
        idlayanan = request.POST['idlayanan']
        idtransaksi = gettransaksi
        idlayanan = getlayanan
        gettransaksi = models.transaksi.objects.get(idtransaksi = idtransaksi)
        getlayanan = models.layanan.objects.get(idlayanan = idlayanan)
        transaksiobj = gettransaksi
        layananobj = getlayanan

        newdetaillayanan = models.detaillayanan(
            idtransaksi = idtransaksi,
            idlayanan = idlayanan,
        )
        newdetaillayanan.save()
        return redirect('index')

def updatedetaillayanan(request):
    detaillayananobj = models.layanan.objects.get(iddetaillayanan=id)
    if request.method == 'GET':
        return render(request, 'updatedetaillayanan.html', {
            'detaillayanan':detaillayananobj
        })
    elif request.method == 'POST':
        idtransaksi = request.POST['idtransaksi']
        idlayanan = request.POST['idlayanan']
        detaillayananobj.idtransaksi = idtransaksi
        detaillayananobj.idlayanan = idlayanan
        return redirect('detaillayanan')

def deletedetaillayanan(request,id):
    detaillayananobj = models.detaillayanan.objects.get(iddetaillayanan=id)
    detaillayananobj.delete()
    return redirect('index')