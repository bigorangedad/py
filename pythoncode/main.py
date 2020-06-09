
have_girl = False


def send():

    global have_girl
    print("发女朋友啦..")
    have_girl = True
    ##print(f"have_girl ={have_girl}")

def show():
    if have_girl == True:
        print("有女朋友，好开心~~")

    else:
        print("单身贵族 *_*")


##print(__name__)
if __name__ == '__main__':
    send()
    show()



