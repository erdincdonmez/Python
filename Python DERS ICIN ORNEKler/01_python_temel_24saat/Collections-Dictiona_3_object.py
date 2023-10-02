#sözlükler de obje 
ogrenciler={
    "Erdinç":{"Memleketi":"Kayseri","Telefonu":"05079438357"},
    "Erhan" :{"Memleketi":"İzmir","Telefonu":"05686254862"},
    "Ensar" :{"Memleketi":"Trabzon","Telefonu":"05223625487"},
    "Esma"  :{"Memleketi":"Hakkari","Telefonu":"05423256988"},
    "Ergün" :{"Memleketi":"Edirne","Telefonu":"05558569874"},
    }

print ("Erhan'ın numarası : ",ogrenciler["Erhan"])

#ogrenciler["Erhan"]="05554448899" # diğer değerleri siler
ogrenciler["Erhan"]={"Memleketi":"İzmir","Telefonu":"05554448899"},


print ("Erhan'ın numarası değişti:",ogrenciler["Erhan"])
