import json

mahasiswa = []

arin = {"nama": "Arin", "alamat": "Tegal"}
tyas = {"nama": "Tyas", "alamat": "Tegal"}
hetsbi = {"nama": "Hetsbi", "alamat": "Kramat"}

mahasiswa.append(arin)
mahasiswa.append(tyas)
mahasiswa.append(hetsbi)

json_str = json.dumps(mahasiswa)
print(json_str)