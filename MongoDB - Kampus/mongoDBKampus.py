import pymongo
dburl = "mongodb://localhost:27017"
myMongo = pymongo.MongoClient(dburl)
dbs = myMongo.list_database_names()

# print(dbs) #Checking list of data base making suere kampus is already made before int he CMD
# I made 2 users and inserted a single data to each collection so it will help me work in python to find
# the collection

kampusdb = myMongo["Kampus"]
# print(kampusdb.list_collection_names()) #Making sure that collection name ["Dosen", "Mahasiswa"] is already here
""" =============================================== Inseerting Dosen Collection ========================== """
dosen_collection = kampusdb["Dosen"]

# for i in dosen_collection.find():
#     print(i) #checking the input of CMD {"Nama" : "Teguh Dosen"} is here 

# dosen_collection.insert_many([{"nama":"Caca",
# "usia":28,
# "asal":"Jakarta",
# "bidang":"Fisika Astrologi",
# "titel":"S2",
# "status":"Honorer",
# "nip":123,
# "matkul":["Metrologi","Kosmologi","Kalkulus"]},
# {"nama":"Dedi",
# "usia":29,
# "asal":"Yogyakarta",
# "bidang":"Fisika Terapan",
# "titel":"S3",
# "status":"PNS",
# "nip":456,
# "matkul":["Instrumentasi","Elektronika","Fisika Dasar"]},
# {"nama":"Euis",
# "usia":30,
# "asal":"Bandung",
# "bidang":"Fisika Teoretik",
# "titel":"S1",
# "status":"Honorer",
# "nip":789,
# "matkul":["Fisika Dasar","Fisika Modern","Kalkulus"]}])

# print("insert process sucess") # since python code is line by line if the terminal print this means the
                               # insert in succesfully happened

""" =================== Always Comment after insert to make sure it double insert doesn't happened ==================="""



# dosen_collection.delete_one({"Nama" : "Teguh Dosen"}) # This was the user i made on CMD before

# print("Delete Succesfully") # Checking the delete process

# for i in dosen_collection.find():
#     print(i) # Check all the value in the collection dosen

""" ========================================= Inserting Datas to Mahasiswa collection =================== """
collection_mahasiswa = kampusdb["Mahasiswa"]

# collection_mahasiswa.insert_many([{"nama":"Faza",
# "usia":19,
# "asal":"Aceh",
# "prodi":"Fisika",
# "angkatan":2017,
# "nim":123},
# {"nama":"Gilang",
# "usia":20,
# "asal":"Semarang",
# "prodi":"Fisika",
# "angkatan":2017,
# "nim":456},
# {"nama":"Hanafi",
# "usia":20,
# "asal":"Makassar",
# "prodi":"Fisika",
# "angkatan":2017,
# "nim":789},
# {"nama":"Dini",
# "usia":20,
# "asal":"Bekasi",
# "prodi":"Fisika",
# "angkatan":2017,
# "nim":"004"}])

# print("Insert Mahasiswa Success")

""" Always Comment after you insert """

""" ========================== Deleting Faza =================================================== """

# collection_mahasiswa.delete_one({"Nama" : "Teguh Mahasiswa"}) deleting data that i input on the cmd before

# print("delete success") Checking deletion process

# for i in collection_mahasiswa.find():
#     print(i) # Check the ddatas in the collection Mahasiswa

# collection_mahasiswa.delete_one({"nama" : "Faza"}) # Dropping Faza as requested byee Faza :(

# print("Faza is Dropped Out :(") #Making sure Faza is  dropped out / deleted

# for i in collection_mahasiswa.find():
#     print(i) 
""" =============== Inserting Dodi to Dosen ==================== """
# dosen_collection.insert_one({"nama":"Dodi",
# "usia":27,
# "asal":"Surabaya",
# "bidang":"Computer Science",
# "titel":"S2",
# "status":"PNS",
# "nip":998,
# "matkul":["Data Analysis","AI","NLP"]})

# print("Dodi is in Dosen Collection")

# for i in dosen_collection.find():
#     print(i)

""" ========== Update Hanafi Name and Age =================== """

# collection_mahasiswa.update_one({"nama" : "Hanafi"}, {"$set":{"nama" : "Ahmad Hanafi"}})
# collection_mahasiswa.update_one({"nama" : "Ahmad Hanafi"}, {"$set":{"usia" : 22}})

# print("Hanafi succesfully updated ")

# for i in collection_mahasiswa.find():
#     print(i)


""" ========= update Students who's 20 y/o to math major =========== """
# collection_mahasiswa.update_many({"usia" : 20}, {"$set":{"prodi": "Matematika"}})
# print('Update Major changes success')


""" ======== Rename Property asal to kota asal ====================="""
# collection_mahasiswa.update_many({},{"$rename":{"asal" : "kota_asal"}})
# print("Update Succeed")

""" ============ Trying to Change Dini nim into int but doesnt work ============== """
nomer_induk = str(4)
nomer_induk_zero = nomer_induk.zfill(3)
# print(nomer_induk_zero)
# collection_mahasiswa.update_one({"nama" : "dini"}, {"$set": {"nim" : nomer_induk_zero}})
# print("update dini success")
for i in collection_mahasiswa.find():
    print(i)

print("004".isdigit())