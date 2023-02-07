

def files():

    file_n = input("File name: ").strip().lower()
    file_i = file_n[-4:]


    if file_i == ".gif":
        print("image/gif")

    elif file_i == ".jpg":
        print("image/jpeg")

    elif file_i == "jpeg":
        print("image/jpeg")

    elif file_i ==  ".png":
        print("image/png")

    elif file_i ==  ".pdf":
        print("application/pdf")

    elif file_i ==  ".txt":
        print("text/plain")

    elif file_i ==  ".zip":
        print("application/zip")

    else:
        print("application/octet-stream")

files()