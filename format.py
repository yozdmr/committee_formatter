import json

def write_chairs(chairs, f):
    write_chair = 0
    for chair in chairs:
        if chair == 'Chair and' and write_chair == 0:
            f.write("<p><strong>Chair and Dean's Liaison</strong></p>\n")
            write_chair = -1
        else:
            f.write("<p><strong>Chair</strong></p>\n")
            write_chair = 1
            if chair != "":
                if ": " in chair:
                    chair = chair.split(": ")[1]
                f.write(f"<p>{chair}</p>\n")
        
        return write_chair

# Fix liaison showing up sometimes
def write_liaison(liaison, f, write_chair):
    if write_chair == 1:
        f.write("<p><strong>Dean's Liaison</strong></p>\n")
    cleaned_liaison = liaison
    if ": " in liaison:
        s = liaison.split(": \t")
        if len(s) < 2:
            s = liaison.split(":  \t")
        cleaned_liaison = s[1]
    f.write(f"<p>{cleaned_liaison}</p>\n")

def write_members(members, f):
    f.write("<p><strong>Members</strong></p>\n<ul>")
    for m in members:
        if m != "" and m != "Members:":
            if ": " in m:
                m = m.split(": ")[1]
            f.write(f"<li>{m}</li>\n")
    f.write("</ul>")

def write_alternates(alternates, f):
    f.write("<p><strong>Alternates</strong></p>\n<ul>")
    for a in alternates:
        if a != "" and a != "Alternates:":
            if ": " in a:
                a = a.split(": ")[1]
            f.write(f"<li>{a}</li>\n")
    f.write("</ul>")

# Fix charges on separate lines
def write_charge(charge, f):
    f.write("<p><strong>Committee Charge</strong></p>\n<ol>")
    for i in range(len(charge)-1):
        c = charge[i]
        if c != "" and c != "Committee Charge:":
            if ": " in c:
                c = c.split(": ")[1]
            # Issue below
            f.write(f"<li>{c}")
            if '\t' not in charge[i+1]:
                f.write("</li>\n")
    f.write("</ol>")

data = json.load(open('bin/committee_list.json'))

switch = True
with open("bin/code.txt", "w") as f:
    for i in range(1):
        if i == 1 and switch:
            f.write("\n\n\nAd Hoc Committees\n")
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


                f.write("\n---------------------------\n")

        

f.close()
'''

<p><strong>Chair</strong></p>
<p>Matthew Wieland (ACC) (2023)</p>
<p><strong>Dean's Liaison</strong></p>
<p>Chanelle White</p>
<p><strong>Members</strong></p>
<ul>
<li>EJ Ume (ECO) (2025)</li>
<li>David Gempesaw (FIN) (2025)</li>
<li>Mark Lacker (ESP) (2023)</li>
<li>John Ni (MGT) (2025)</li>
<li>Pat Schur (ISA) (2024)</li>
<li>Peter Nguyen (MKT) (2025)</li>
</ul>
<p><strong>Alternates</strong></p>
<ul>
<li>James Zhang (ACC) (2025)</li>
<li>Nam Vu (ECO) (2025)</li>
<li>Geoff Zoeckler (ESP) (2025)</li>
<li>Yvette Harman (FIN) (2025)</li>
<li>Michael Gowins (ISA) (2025)</li>
<li>Darryl Rice (MGT) (2025)</li>
<li>Eric Stenstrom (MGT) (2025)</li>
</ul>
<p><strong>Committee Charge</strong></p>
<ol>
<li>Consider academic grievances as outlined in the Student Handbook.</li>
<li>The Committee will meet to address its annual charge. Meeting minutes will be taken.</li>
<li>The Committee Chair will provide a summative year-end report of Committee activities to the Associate Dean for Curriculum. This report will be added as a consent item to the agenda of the first faculty meeting of the following academic year.</li>
</ol>

'''