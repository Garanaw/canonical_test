import data1
import data2
import data3

def exercise1(person, people):
    membership = []
    for t in people:
        if person.belongsToTeam(t):
            membership.append(t)
    return membership

def get_people(team):
    return team.getAllMembersAndSubMembers()

if __name__ == '__main__':
    # Exercise 1
    print([t.displayname for t in exercise1(data1.alice, data1.people)])

    # Exercise 2
    print([t.displayname for t in exercise1(data2.alice, data2.people)])

    # Exercise 3
    print(sorted(p.displayname for p in get_people(data2.c_team)))
    print(sorted(p.displayname for p in get_people(data3.c_team)))
