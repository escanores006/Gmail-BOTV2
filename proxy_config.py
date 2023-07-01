try:
    with open(r'C:\Users\Escanor\Gmail-BOTV2\proxies.txt', 'r') as file:
        proxy = [line.rstrip() for line in file.readlines()]
except FileNotFoundError:
    raise Exception('proxies.txt tidak ada.')
