"""
Output file extension
"""

# Prompt user for filename
filename = input("File name: ")

# Determine filetype extension (trim, lower, split on ".", return last element)
extension = filename.strip().lower().split(".")[-1]

# Output filetype based on extension
match extension:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
