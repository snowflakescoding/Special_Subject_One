"""
Given list of names of candidates in an election. A candidate's name in the list represents a vote cast on the candidate. The winner is the candidate who received the maximum vote. If there is a tie, the winner is the one who has lexicographically smaller name.
Write a Python function named winner(votes) that takes a list of votes in an election as the input and return the name of the winner.
For example:
if votes = ['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john','johnny'] in this case, there are four candidates in the election: johnny has 5 votes casted for him, john has 4 votes, jamie has 3 votes and jackie has two votes. So johnny is the winner.
if votes = ['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john'] in this case, in this case johnny has 4 votes casted for him and so does john. But john is the winner because his name 'john' is lexicographically smaller.

We assume that the input list contains at least one integer and all inputs data are correct.
"""

def winner(votes):
    # store vote counts in a dictionary
    vote_count = {}
    
    # count vote for each candidate
    for vote in votes:
        vote_count[vote] = vote_count.get(vote, 0) + 1
    
    # find max of votes
    max_votes = max(vote_count.values())
    
    # find all candidates with the max votes
    candidate_max_votes = [name for name, count in vote_count.items() if count == max_votes]
    
    # return min lexicographically smallest name
    return min(candidate_max_votes)


print(winner(['trump','biden','biden','biden','trump']))
print(winner(['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john','johnny']))
print(winner(['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john']))

