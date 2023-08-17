import json

def write_chairs(chairs, f):
    write_chair = 0
    if chairs[0] == 'Chair and':
        f.write("<p><strong>Chair and Dean's Liaison</strong></p>\n")
        write_chair = -1
    else:
        chair_type = "Co-Chairs" if "Co-" in chairs[0] else "Chair"
        f.write(f"<p><strong>{chair_type}</strong></p>\n")
        write_chair = 1
        if len(chairs) > 2:
            f.write("<ul>\n")
        for chair in chairs:
            if chair != "":
                if ": " in chair:
                    chair = chair.split(": ")[1]
                if len(chairs) > 2:
                    f.write(f"<li>{chair}</li>\n")
                else:
                    f.write(f"<p>{chair}</p>\n")
        if len(chairs) > 2:
            f.write("</ul>\n")
        
    return write_chair

# Fix liaison showing up sometimes
def write_liaison(liaison, f, write_chair):
    if write_chair == 1:
        f.write("<p><strong>Dean's Liaison</strong></p>\n")
    cleaned_liaison = liaison
    if ": " in liaison:
        # There is a better way to do this .sfkergjpiowjpoisjreiojgijoijgwe
        s = liaison.split(":\t")
        if len(s) < 2:
            s = liaison.split(": \t")
        if len(s) < 2:
            s = liaison.split(":  \t")
        cleaned_liaison = s[1]
    f.write(f"<p>{cleaned_liaison}</p>\n")

def write_members(members, f):
    f.write("<p><strong>Members</strong></p>\n<ul>\n")
    for m in members:
        if m != "" and m != "Members:":
            if ": " in m:
                m = m.split(": ")[1]
            f.write(f"<li>{m}</li>\n")
    f.write("</ul>\n")

def write_alternates(alternates, f):
    f.write("<p><strong>Alternates</strong></p>\n<ul>\n")
    for a in alternates:
        if a != "" and a != "Alternates:":
            if ": " in a:
                a = a.split(": ")[1]
            f.write(f"<li>{a}</li>\n")
    f.write("</ul>\n")

def write_charge(charge, f):
    f.write("<p><strong>Committee Charge</strong></p>\n<ol>\n")
    i = 0
    while i < len(charge)-1:
        c = charge[i]
        d = charge[i+1]

        if c != "" and c != "Committee Charge:":
            if ": " in c:
                print(f"A|{c}|")
                c = c.split(": ")[1]
                print(f"B|{c}|")
            if '\t' in d or d[:4] == 'Dean':
                f.write(f"<li>{c} {d}</li>\n")
                i+=1
            else:
                f.write(f"<li>{c}</li>\n")
        i+=1
            
    f.write("</ol>\n")


def format_doc(file):
    file_name = file.split(".")[0]
    data = json.load(open(f'bin/{file_name}.json'))

    switch = True
    with open(f"output/result_{file_name}.html", "w") as f:
        for i in range(2):
            if i == 1 and switch:
                f.write("\n\n\n<br><br>Ad Hoc Committees<br><br>\n")
                switch = False

            for c in data[i]:
                if len(c.keys()) > 0:
                    f.write(f"\n-----|| {c['name']} ||-----\n")
                    write_chair = write_chairs(c['chairs'], f)

                    if 'liaison' in c.keys():
                        write_liaison(c['liaison'], f, write_chair)
                    
                    if 'members' in c.keys():
                        write_members(c['members'], f)
                    
                    if 'alternates' in c.keys():
                        write_alternates(c['alternates'], f)

                    write_charge(c['charge'], f)


                    f.write("\n---------------------------<br>\n")

    f.close()