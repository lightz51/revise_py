def main():
    filename = input("Filename: ").strip().split(".")[-1].lower()

    match filename:
        case "gif" | "jpg" | "jpeg" | "png":
            print(f"media/{filename}")
        case "pdf" | "zip":
            print(f"application/{filename}")
        case ("txt"):
            print("text/plain")
        case _:
            print("application/octet-stream")

# Alternative way
    # filename = input("Filename: ").strip().lower()

    # if filename.endswith(".gif"):
    #     print("media/gif")
    # elif filename.endswith(".jpg"):
    #     print("media/jpg")
    # elif filename.endswith(".jpeg"):
    #     print("media/jpeg")
    # elif filename.endswith(".png"):
    #     print("media/png")
    # elif filename.endswith(".pdf"):
    #     print("application/pdf")
    # elif filename.endswith(".txt"):
    #     print("text/plain")
    # elif filename.endswith(".zip"):
    #     print("application/zip")
    # else:
    #     print("application/octet-stream")

if __name__ == "__main__":
    main()