import os
import csv

csvpath = os.path.join("C:/PREWORK_AS/Module-3/Python_challenge-master/Python_challenge-master/PyPoll/main.py/03-Python_Instructions_PyPoll_Resources_election_data (1).csv")

t_votes = 0
number_candidates = 0
candidate_list = []
candidate_votes = {}
maxvotes = -1

with open(csvpath, newline='') as csvfile:

   
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        current_candidate = row[2]
        if current_candidate not in candidate_list:
            number_candidates=number_candidates+1
            candidate_list.append(current_candidate)
            candidate_votes[current_candidate]=0

        candidate_votes[current_candidate]=candidate_votes[current_candidate]+1
        t_votes=t_votes+1

        if candidate_votes[current_candidate] > maxvotes :
            maxvotes = candidate_votes[current_candidate]
            maxcandidate = current_candidate
line1 = '  Election Results'
line2 = '  -------------------------'
line3 = ('  Total Votes: %d' %(t_votes))
line4 = '  -------------------------'
output = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

for name in candidate_list :
    linex = ('  %s: %.3f%% (%d)' %(name,  100*candidate_votes[name]/(0.0+t_votes), candidate_votes[name]))
    output = output + '\n' + linex

output = output + '\n' + '  -------------------------'
output = output + '\n' + ('  Winner: %s' %maxcandidate)
output = output + '\n' + '  -------------------------'

print(output)






