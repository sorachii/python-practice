with open('name.txt', 'r') as name, \
     open('surname.txt', 'r') as sname, \
     open('full_name.txt', 'w') as fname:
    for ln in name.readlines():
        fname.write((ln.strip() + " " + sname.readline()))
