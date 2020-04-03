# To see the original code assignment [click here](ASSIGNMENT.md)

# My Approach

I was not really sure if the provided files were to be modified, however I wanted to take a real OOP approach, which involves some aditions in the Person class to provide a bit of behavior.

## Task 1:

The provided solution checks if the provided Person belongs to the provided Team (in case it is a Team) by asking the Person itself.

## Task 2:

Part of the code writen for the first task has been modified to recursively call the same method in the subsequent teams (called sub-teams in the code). Also, a few extra helper methods have been added to determine whether the target object is a Team and to extract both, Teams and Members that are not teams.

## Task 3

By inspecting the provided data fixtures, I could understand that the requirement is to retrieve all the members that belongs to the passed in team AND all the members that belongs to the sub-teams in the passed in team.

This has been resolved with a similar approach than the previous task: applying recursion. The problem I had to face here was when checking for the members in the data3 fixture: as I could see, there is a circular reference in the teams. This was solved by setting a checkpoint at the begining of the process that matches the initial team. Once the whole circle has been completed, an empty list is returned (there is no need to still check for the members of the current team, as they are listed at the end of the process anyways).

# Personal thoughts:

After a few years without touching Python, it has been really fun to come back to the language. Also, the task itself was an interesting problem to solve.
