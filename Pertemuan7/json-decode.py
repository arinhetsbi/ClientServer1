import json

data = '[{ "nama" : "Ariningtyas", "alamat" : "Jatilawang Kramat" },' \
       '{ "nama" : "Hetsbi", "alamat" : "Tegal" }]'

result = json.loads(data)

for x in result:
    print(x['nama'])