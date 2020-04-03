class Person(object):

    def __init__(self, id, displayname, members=None):
        self.id = id
        self.displayname = displayname
        self.members = members
        self.is_team = members is not None

    def isTeam(self):
        """
        Returns True if the Person object is a team, False otherwise
        """
        return self.is_team == True

    def isPerson(self):
        """
        Returns True if the Person object is NOT a team, False otherwise
        """
        return self.is_team == False

    def getMembersThatAreTeams(self):
        """
        Returns a filtered list with all the members that belongs to the 
        team that are also a team
        """
        if self.isPerson():
            raise Exception('%s is not a team', self.displayname)
        return list(filter(lambda t: t.isTeam(), self.members))

    def getMembersThatAreNotTeams(self):
        """
        Returns a filtered list with all the members that belongs to the 
        team that are not a team
        """
        if self.isPerson():
            raise Exception('%s is not a team', self.displayname)

        return list(filter(lambda p: p.isPerson(), self.members))

    def getAllMembersAndSubMembers(self, startingTeam = None):
        """
        Returns a filtered list with all the members that belongs to the
        team and sub-teams
        """
        if self.isPerson():
            raise Exception('%s is not a team', self.displayname)

        # Checkpoint to control the recursion level
        if startingTeam != None and startingTeam.id == self.id:
            return []

        # If no team is passed, set the current one as a start point to check the recursion level
        if startingTeam == None:
            startingTeam = self

        subMembership = list(map(lambda subteam: subteam.getAllMembersAndSubMembers(startingTeam), self.getMembersThatAreTeams()))

        if subMembership == []:
            return self.getMembersThatAreNotTeams()

        for i in self.getMembersThatAreNotTeams():
            subMembership[0].append(i)

        return subMembership[0]

    def belongsToTeam(self, people):
        """
        Determines if the Person objects belongs to the given team
        """
        # If the passed "team" is an actual person, we're done here
        if people.isPerson():
            return False

        # If the person belongs to the passed in team, there's no need to
        # check for a sub-membership, a higher membership prevails
        if people.members.__contains__(self):
            return True

        teams = people.getMembersThatAreTeams()

        # If none of the members in the passed in team is a team, there's
        # no sub-membership to check
        if teams == []:
            return False

        # Now that we have the sub-teams, we will recursively check if
        # the Person belongs to any of them
        for team in teams:
            if self.belongsToTeam(team):
                return True

        return False
