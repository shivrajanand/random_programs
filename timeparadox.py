loop_count = 0

grandfather_born = True
grandfather_alive = True
father_born = True
traveler_born = True
time_machine_created = True
go_to_past = True
killed_grandfather = True
who_killed_grandfather = 1 #0 means we dont know 1 means we knowsubtitle

while loop_count != 10:
    if traveler_born:
        time_machine_created = True
        who_killed_grandfather = 1
    else:
        time_machine_created = False
        who_killed_grandfather = 0


    if time_machine_created:
        go_to_past = True
    else:
        go_to_past = False


    if go_to_past:
        killed_grandfather = True
    else:
        killed_grandfather = False


    if killed_grandfather:
        father_born = False
    else:
        father_born = True

    if father_born:
        traveler_born = True
    else:
        traveler_born = False

    print("loop_count: ", loop_count)
    print("grandfather_born: ", grandfather_born)
    print("grandfather_alive: ", grandfather_alive)
    print("father_born: ", father_born)
    print("traveler_born: ", traveler_born)
    print("time_machine_created: ", time_machine_created)
    print("go_to_past: ", go_to_past)
    print("killed_grandfather: ", killed_grandfather)
    print("who_killed_grandfather: ", who_killed_grandfather)

    print("\n"*5)


    loop_count += 1




