import os

PATH = "../Menu Text/"

def decode(sort_path):
    """sort"""
    final_path = PATH + sort_path
    write_path = PATH + "Decoded/"
    decoded = []
    for filename in os.listdir(final_path):
        path_a = os.path.join(final_path, filename)
        with open(path_a,'r',encoding='utf8') as f:
            for line in f:
                decoded += line.encode('utf8').decode('utf8')

        path_b = os.path.join(write_path, filename)
        with open(path_b,'w',encoding='utf8') as f:
            for data in decoded:
                f.write(data)

decode("Translated/")
