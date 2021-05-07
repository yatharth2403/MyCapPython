name = input("Enter the full name of the file: ")
ext = name.split('.')[1]
print("The extension of the file is: .", ext, "\n")
print("File type is: ")
if ext == "exe":
    print("Executable file")
elif ext == "doc" or ext == "docx":
    print("Word file")
elif ext == "py":
    print("Python file")
elif ext == "c":
    print("C file")
elif ext == "cpp":
    print("C++ file")
elif ext == "txt":
    print("Text file")
