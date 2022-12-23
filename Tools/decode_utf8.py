import os

PATH = "../Menu Text/"

def decode(sort_path):
    """sort"""
    final_path = PATH + sort_path
    write_path = PATH + "Decoded/"
    for filename in os.listdir(final_path):

        decoded = []
        path_a = os.path.join(final_path, filename)
        with open(path_a,'r',encoding='utf-8') as f:
            for line in f:
                decoded += line.encode('utf-8').decode('unicode-escape', 'replace')

        path_b = os.path.join(write_path, filename)
        with open(path_b,'w', encoding='utf-8') as f:
            for data in decoded:
                try:
                    f.write(data)
                except UnicodeEncodeError:
                    print("Error")

decode("Translated/")
