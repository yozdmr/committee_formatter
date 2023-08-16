    f.write(f"\n-----|| {c['name']} ||-----\n")
                if 'chairs' in c.keys():
                    write_chair = write_chairs(c['chairs'], f)

                if 'liaison' in c.keys():
                    write_liaison(c['liaison'], f, write_chair)
                
                if 'members' in c.keys():
                    write_members(c['members'], f)


                f.write("\n---------------------------\n")