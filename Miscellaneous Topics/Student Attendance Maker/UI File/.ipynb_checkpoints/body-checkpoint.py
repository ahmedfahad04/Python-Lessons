import datetime

def take_attendance(input_data, input_file):
    std_info = {'abhijit': 1201, 'mashiat': 1202, 'shazzad': 1203, 'fahad': 1204, 'tasnia': 1205, 'shaed': 1206,
                'sazzad': 1207, 'rupali': 1208, 'sakib': 1209, 'rakibul': 1210, 'sharif': 1211, 'abdullah': 1212,
                'rifah': 1213, 'swarna': 1214, 'muktadul': 1215, 'sadia': 1216, 'kamruzzaman': 1217, 'dipshikha': 1218,
                'sampad': 1219, 'yasir': 1220, 'sifat': 1221, 'maimuna': 1222, 'tashfia': 1223, 'hasib': 1224,
                'nazmus': 1225, 'rufidatul': 1226, 'momenuzzaman': 1227, 'monayem': 1228, 'abir': 1229, 'arnab': 1230,
                'fahim': 1231, 'ahnaf': 1232, 'mehzabin': 1233}

    std_attendance = {}

    with open(input_file, 'r') as file:  # 1. take the previous attendance
        x = file.readlines()
        total_present = 0

        for item in x:
            name = (item.lower()).split("_")[0]  # names
            k = item[::-1]
            if name in std_info:

                t = (k.split(" :")[0]).strip("\n")  # checking for skipping blank lines

                if "0" <= t <= "9":
                    n = ((k.split(" :")[0]).lstrip('\n'))
                    if (name.title() in input_data) or (name.lower() in input_data):
                        total_present += 1
                        std_attendance[name.lower()] = int(n)+1  # 2. update attendance
                    else:
                        std_attendance[name.lower()] = int(n)
            else:
                pass

    #print("Total Present: " + str(total_present))
    file.close()


    with open(input_file, 'w+') as file:  # 3. writing the upadated attendance in intermediate file txt

        for key, val in std_attendance.items():
            ans = key.title() + "_" + str(std_info[key]) + ": " + str(std_attendance[key]) + "\n"

            file.write(ans)

        x = datetime.datetime.now()
        k = "\nLast Update: " + str(x.strftime('%Y/%m/%d %I:%M:%S'))
        file.write(str(k))
        print(x)

    return


