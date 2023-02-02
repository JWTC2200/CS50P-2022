file = input("File name:")

split = file.rsplit(".")
exten = split[-1].replace(" ", "").lower()

if exten == "gif":
    print("image/gif")

elif exten == "jpg":
    print("image/jpeg")

elif exten == "jpeg":
    print("image/jpeg")

elif exten == "png":
    print("image/png")

elif exten == "pdf":
    print("application/pdf")

elif exten == "txt":
    print("text/plain")

elif exten == "zip":
    print("application/zip")

else:
    print("application/octet-stream")
