File_input = input("File name: ").lower().replace(" ", "")


if File_input.endswith("gif") or File_input.endswith("png"):
    File_input = File_input.split(".")[-1]
    print(f"image/{File_input}")

elif File_input.endswith("jpg") or File_input.endswith("jpeg"):
    print("image/jpeg")

elif File_input.endswith("zip") or File_input.endswith("pdf"):
    File_input = File_input.split(".")[-1]
    print(f"application/{File_input}")

elif File_input.endswith("txt"):
    print("text/plain")

else:
    print("application/octet-stream")