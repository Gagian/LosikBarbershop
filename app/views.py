from multiprocessing import dummy
import re
from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home (request):
    allpelayanobj = models.pelayan.objects.all()
    alllayananobj = models.layanan.objects.all()
    return render(request, 'dashboard.html',{
        "allpelayanobj" : allpelayanobj,
        "alllayananobj" : alllayananobj
    })
def pelayan (request):
    allpelayanobj = models.pelayan.objects.all()
    # getpelayanobj = models.pelayan.objects.get(idpelayan=)

    return render(request, 'tablepelayan.html',{
        "allpelayanobj" : allpelayanobj,
        # "getpelayanobj" : getpelayanobj,
    })

def layanan (request):
    alllayananobj = models.layanan.objects.all()
    # getlayananobj = models.layanan.objects.get(idlayanan=1)

    return render(request, 'tablelayanan.html',{
        "alllayananobj" : alllayananobj,
        # "getlayananobj" : getlayananobj,
    })

def transaksi(request):
    data=[]
    alltransaksiobj = models.transaksi.objects.all()
    for item in alltransaksiobj:
        dummy=[]
        id_transaksi = item.idtransaksi
        servicedetail = models.detaillayanan.objects.filter(idtransaksi = id_transaksi)
        dummy.append(item)
        dummy.append(servicedetail)
        data.append(dummy)

<<<<<<< HEAD
    return render(request, 'tabletransaksi.html',{
=======
    return render(request, 'transaksi.html',{
>>>>>>> e32aeef3b018835db6eb841ec718c205d4ccd49e
        "transaksi" : data
    })


def detaillayanan (request,id):
    detaillayananobj = models.detaillayanan.objects.filter(idtransaksi = id)
    alldetaillayananobj = models.detaillayanan.objects.all()

<<<<<<< HEAD
    return render(request, 'tabledetaillayanan.html',{
=======
    return render(request, 'detaillayanan.html',{
>>>>>>> e32aeef3b018835db6eb841ec718c205d4ccd49e
        "alldetaillayananobj" : detaillayananobj,
        'service_detail': detaillayananobj
    })

def createdatapelayan(request):
    if request.method == 'GET':
        return render(request, 'formaddpelayan.html')
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
        return render(request,'formupdatepelayan.html',{
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
        return render(request, 'formaddlayanan.html')
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
        return render(request,'formupdatelayanan.html',{
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
        return render(request, 'formcreatetransaksi.html',{
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
    transaksiobj = models.transaksi.objects.get(idtransaksi=id)
    pelayanobj= models.pelayan.objects.all()
    if request.method == "GET":
<<<<<<< HEAD
        return render(request,'formupdatetransaksi.html',{
=======
        return render(request,'updatetransaksi.html',{
>>>>>>> e32aeef3b018835db6eb841ec718c205d4ccd49e
            'gettransaksiobj':transaksiobj,
            'pelayan' :pelayanobj
        })
    else:
        idpelayan = request.POST['idpelayan']
        getpelayan = models.pelayan.objects.get(idpelayan = idpelayan)
        transaksiobj.idpelayan = getpelayan
        transaksiobj.namapelanggan = request.POST['namapelanggan']
        transaksiobj.tanggaltransaksi = request.POST['tanggaltransaksi']
        transaksiobj.save()
        return redirect('transaksi')

def deletetransaksi(request,id):
    transaksiobj = models.transaksi.objects.get(idtransaksi=id)
    transaksiobj.delete()
    return redirect('transaksi')

def createdetaillayanan(request):
    layananobj = models.layanan.objects.all()
    transaksiobj = models.transaksi.objects.all()
    if request.method == "GET":
<<<<<<< HEAD
        return render(request, 'formdetaillayanan.html', {
=======
        return render(request, 'createdetaillayanan.html', {
>>>>>>> e32aeef3b018835db6eb841ec718c205d4ccd49e
            'layanan' : layananobj,
            'transaksi' : transaksiobj
        })
    else:
        idtransaksi = request.POST['idtransaksi']
        jenislayanan = request.POST['idlayanan']
        gettransaksi = models.transaksi.objects.get(idtransaksi = idtransaksi)
        getlayanan = models.layanan.objects.get(idlayanan = jenislayanan)
        newdetaillayanan = models.detaillayanan(
            idtransaksi = gettransaksi,
            idlayanan = getlayanan
        ).save()

        return redirect('transaksi')

def updatedetaillayanan(request,id):
    detaillayanan = models.detaillayanan.objects.get(iddetaillayanan = id)
    print(detaillayanan)
    updatedetaillayanan_obj = models.layanan.objects.all()
    if request.method == "GET":
<<<<<<< HEAD
        return render(request, 'formupdatedetaillayanan.html', {
=======
        return render(request, 'updatedetaillayanan.html', {
>>>>>>> e32aeef3b018835db6eb841ec718c205d4ccd49e
            'updatedetaillayanan': updatedetaillayanan_obj,
            'detaillayananobj': detaillayanan
        })
    else:
        idlayanan = request.POST['idlayanan']
        layananobjget = models.layanan.objects.get(idlayanan=idlayanan)
        detaillayanan.idlayanan = layananobjget

        detaillayanan.save()
        return redirect('transaksi')

def deletedetaillayanan(request,id):
    deletedetaillayanan = models.detaillayanan.objects.get(iddetaillayanan =id)
    deletedetaillayanan.delete()
    return redirect('transaksi')