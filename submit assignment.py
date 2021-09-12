def submit_assignment(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik. 
    Lalu menampilkan semua activity bertipe assignment di topik tersebut, lalu meminta user memilih activity assignment.
    Jika nim sudah submit di assignment yang dipilih, maka tampilkan pesan batal submit.
    Jika nim belum submit, minta jawaban assignment dan simpan jawaban di data submission.
    '''
    
    print('----Fungsi "submit_assignment" dijalankan----')
    list_index=[]
    for index, value in enumerate(list_topic):
        index +=1
        list_index.append(index)
        print(f'{index}. {value["Title"]}')
    try:
        topic = int(input("Masukkan nomor topic: "))
        if topic in list_index:
            print("Berikut ini adalah list assignment: ")
            print("ID\t\t|Title\t\t\t\t|Type\t\t\t|Description")
            print("-"*100)
            for i in list_topic[topic - 1]["Activities"]:
                if dict_activity[i]['Type'] == "assignment":
                    print(f"{i}\t\t|{dict_activity[i]['Title']}\t\t|{dict_activity[i]['Type']}\t\t|{dict_activity[i]['Description']}")
                    try: 
                        IDAssignment = int(input("Masukkan ID assignment: "))
                        if IDAssignment == i:
                            for key, value in dict_submission.items():
                                key=i
                                if nim in dict_submission[key]:
                                    print("Submit dibatalkan, Anda sudah submit sebelumnya.")
                                    break
                                else:
                                    try:
                                        JawabanAssignment = input("Masukkan jawaban assignment: ")
                                        dict_submission[IDAssignment][nim] = JawabanAssignment
                                        print("Submission berhasil")
                                        break
                                    except:
                                        print("Maaf, input salah. Harap diulang kembali.")
                        else:
                            print("Maaf, input salah. Harap diulang kembali.")
                    except:
                        print("Maaf, input salah. Harap diulang kembali.")
        else:
            print("Maaf, input salah. Harap diulang kembali.")
        
    except:
        print("Maaf, input salah. Harap diulang kembali.")
   

    print("\n\n")
    print("Tekan Enter untuk kembali ke menu utama...")

if __name__ == "__main__":
    LAST_ID_ACTIVITY = 2
    NIM_LOGIN = ''
    ADMIN_LOGIN = False


    #key pada dict_mhs['data'] adalah NIM
    dict_mhs = {'field' : [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                           ('Email', '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                           ('Password', '^[a-zA-Z0-9]{8,12}$')],
             'data' : {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                       '114': {'Nama': 'Joni', 'Email': 'joni@telU.com', 'Password': '12345678'},
                       '115': {'Nama': 'jeje', 'Email': 'jeje@telU.com', 'Password': '12345678'}

                       }           
            }

    #Value pada key 'Activities' berupa list berisi id_activity
    list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0, 1]},
                    {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}
                  ]

    # key pada dict_activity adalah id_activity 
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                         1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                         2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                         }

    # key pada dict_submission adalah id_activity 
    dict_submission = {0: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                        2: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'}
                       }

    # key pada dict_grade adalah id_activity 
    dict_grade = {0: {'113' : 100}
                        
                  }
