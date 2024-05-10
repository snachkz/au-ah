def save(data, parent_folder='./data'):
    import os
    import csv

    folder_name = input("Masukkan nama folder: ")
    path_folder = os.path.join(parent_folder, folder_name)
    #check folder sudah ada atau belum
    if not os.path.exist(path_folder):
         #folder belum ada jadi membuat folder baru
        os.makedirs(path_folder)   
        print (f"Membuat folder data {path_folder} ")

    #cek folder kosong atau tidak
    files = os.listdir(path_folder)     
    if len(files) == 0:
        #jika folder kosong, buat file baru
        file_path = os.path.join(path_folder, 'data.csv')
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print (f"Berhasil menyimpan data fi folder data {path_folder}")

    else:
        #jika folder tidak kosong, overwrite file yang sudah ada
        for file in files:
            if file.endswith ('csv'):
                file_path = os.path.join(path_folder, file)
                with open(file_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                print(f"Berhasil menyimpan data di folder data {path_folder}!")
                break





    