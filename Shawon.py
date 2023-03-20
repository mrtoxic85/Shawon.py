def reg():

    os.system('termux-setup-storage')

    os.system('clear')

    os.system('xdg-open https://www.facebook.com/Abal.Not.Allow4685')

    logo()

    print ('')

    print ('                     Checking Approval')

    time.sleep(1) 

    try:

        to = open('/sdcard/Android/.MP0nt.txt', 'r').read()

    except (KeyError, IOError):

        reg2()

    r = requests.get('https://github.com/mrtoxic85/File/blob/main/Approved.txt').text

    if to in r:

        time.sleep(2)

        bsn_menu()

    else:

        os.system('clear')

        os.system('xdg-open https://www.facebook.com/Abal.Not.Allow4685')

        logo()

        print('')

        print ('               \tApproved Not Detected')

        print ('')

        print("            \033[1;97mTHIS TOOL IS PAID YOU NEED TO GET APPROVED FIRST")

        print ('               \033[1;97mYOUR KEY : ' + to)

        print("               COPY AND SEND KEY TO ADMIN")

        name = input("               YOUR NAME : ")

        input('\033[1;97m               PRESS ENTER  TO SEND TOKEN')

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+to

        os.system('am start https://wa.me/+8801641524685?text=' + tks)

        reg()

def reg2():

    os.system('clear')

    logo()

    print('')

    print ('\tApproval Not Detected')

    print('')

    id = uuid.uuid4().hex[:50]

    print("            \033[1;97mTHIS TOOL IS PAID YOU NEED TO GET APPROVED FIRST")

    print ('               \033[1;97mYOUR KEY : ' + id)

    print("               COPY AND SEND KEY TO ADMIN")

    name = input("               YOUR NAME : ")

    input('\033[1;97m               PRESS ENTER  TO SEND TOKEN')

    time.sleep(3.5)

    tks = 'Dear%20MARUF-sir,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+id

    os.system('am start https://wa.me/+8801641524685?text=' + tks)

    sav = open('/sdcard/Android/.MP0nt.txt', 'w')

    sav.write(id)

    sav.close()

    reg()

    r = requests.get('https://github.com/mrtoxic85/File/blob/main/Approved.txt').text
