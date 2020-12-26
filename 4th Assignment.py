myUniqueList = []


def add_to_list(to_add):
    for i in myUniqueList:
        if myUniqueList[i] == to_add:
            return False
        else:
            myUniqueList.append(to_add)
            return True


add_to_list("Razer")
add_to_list("Razer")
add_to_list(1)
add_to_list(1)

print(myUniqueList)
