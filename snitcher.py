import os

large_files = []
def bytes_to_megabytes(size_in_bytes):
    size_in_megabytes = size_in_bytes / (1024 * 1024)
    return round(size_in_megabytes, 2)

def find_large_files():
    for root, files in os.walk("C:/Users/lucas_5q5alx3/Documents/EJEL"):
        for file in files:
            filepath = os.path.join(root, file)
            file_stats = os.stat(filepath)
            file_size = file_stats.st_size
            file_size_in_mb = bytes_to_megabytes(file_size)
            
            if file_size_in_mb > 50:
                large_files.append(filepath)
    #print(f"File: {filepath} Size: {file_size} MB")
    return large_files
large_files = find_large_files()
print(large_files)            