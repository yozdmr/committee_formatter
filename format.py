import json


def check_officio(person):
    return person.replace("ex officio", "<em>ex officio</em>")

def write_note(note, f):
    note = note.split(": ")[1]
    f.write(f"<p><strong>Note: </strong>{note}</p>")

def write_extra(extra, f):
    f.write(f"<p>{extra}</p>")

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
                
                    chair = check_officio(chair)

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
    # liaison = liaison.replace('\t', " ")
    # liaison = ' '.join(liaison.split())
    liaison = liaison.split(": ")[1]
    f.write(f"<p>{liaison}</p>\n")

def write_members(members, f):
    f.write("<p><strong>Members</strong></p>\n<ul>\n")
    for m in members:
        if m != "" and m != "Members:":
            if ": " in m:
                m = m.split(": ")[1]
            
            m = check_officio(m)
            f.write(f"<li>{m}</li>\n")
    f.write("</ul>\n")

def write_alternates(alternates, f):
    f.write("<p><strong>Alternates</strong></p>\n<ul>\n")
    for a in alternates:
        if a != "" and a != "Alternates:":
            if ": " in a:
                a = a.split(": ")[1]

            a = check_officio(a)
            f.write(f"<li>{a}</li>\n")
    f.write("</ul>\n")

def write_charge(charge, f):
    f.write("<p><strong>Committee Charge</strong></p>\n<ol>\n")
    i = 0
    while i < len(charge)-1:
        c = charge[i]
        d = charge[i+1]

        if c != "" and c.strip() != "Committee Charge:":
            if ": " in c:
                c = c.split(": ")[1]
            
            if '\t' in d or d[:4] == 'Dean' or (len(d) > 0 and len(d) > 0 and not d[0].isupper() and c[len(c)-1] != '.'):
                f.write(f"<li>{c} {d}</li>\n")
                i+=1
                    
            else:
                f.write(f"<li>{c}</li>\n")
        i+=1
            
    f.write("</ol>\n")


# Main function
def format_doc(file):
    # Gets the file without the extension, loads JSON file
    file_name = file.split(".")[0]
    data = json.load(open(f'bin/{file_name}.json'))

    switch = True   # Determines when to write "Ad Hoc" to split committee tpes
    # Opens file to output to
    with open(f"output/result_{file_name}.html", "w") as f:
        # Iterates through the two lists, each of which contains committees of a certain category
        for i in range(2):
            # Write when switching to Ad Hoc category
            if i == 1 and switch:
                f.write("\n\n\n<br><br>Ad Hoc Committees<br><br>\n")
                switch = False

            # Iterates through committees
            for c in data[i]:
                # Checks to make sure committee dict is not empty
                if len(c.keys()) > 0:
                    # Writes the committee name
                    f.write(f"\n-----|| {c['name']} ||-----\n")

                    # Writes notes
                    if 'note' in c.keys():
                        write_note(c['note'], f)
                    # Writes extra
                    if 'extra' in c.keys():
                        write_extra(c['extra'], f)
                    
                    # Writes the chair, returns -1 if Chair and Liaison are the same
                    write_chair = write_chairs(c['chairs'], f)

                    # Checks to see if Chair and Liaison are the same, writes liaison
                    if 'liaison' in c.keys():
                        write_liaison(c['liaison'], f, write_chair)
                    
                    # Writes members
                    if 'members' in c.keys():
                        write_members(c['members'], f)
                    
                    # Writes alternates
                    if 'alternates' in c.keys():
                        write_alternates(c['alternates'], f)

                    # Writes charges
                    write_charge(c['charge'], f)


                    f.write("\n---------------------------<br>\n")

    f.close()