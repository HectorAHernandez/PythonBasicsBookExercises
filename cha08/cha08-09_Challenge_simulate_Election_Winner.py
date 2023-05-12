""" this program simulate the winner of the election between two candidates.
There are 3 voting regions. The most recent polls show that candidate A has the
following chances for winning in each region:
    Region 1: 87 percent chance of wining.
    Region 2: 65 percent chance of wining.
    Region 3: 17 percent chance of wining.

This program simulate the election runs 10_000 times and print the percentage of
times in which Candidate A wins.
To keep things simple, assume that a candidate wins the election if they win in
at least two of the three regions.
"""
import random

simulation_number = int(input("Enter the number of simulations: "))

region_1_candidate_a_probability = float(int(input("Enter Candidate A Percent \
chance of winning in Region # 1: ")) / 100)
region_2_candidate_a_probability = float(int(input("Enter Candidate A Percent \
chance of winning in Region # 2: ")) / 100)
region_3_candidate_a_probability = float(int(input("Enter Candidate A Percent \
chance of winning in Region # 3: ")) / 100)

def winner(probability_of_winning):
    if random.random() < probability_of_winning:
        return "Candidate A"
    else:
        return "Candidate B"

region_1_candidate_a_count = 0
region_2_candidate_a_count = 0
region_3_candidate_a_count = 0
region_1_candidate_b_count = 0
region_2_candidate_b_count = 0
region_3_candidate_b_count = 0

for trial in range(simulation_number):
    # region 1:
    if winner(region_1_candidate_a_probability) == "Candidate A":
        region_1_candidate_a_count += 1
    else:
        region_1_candidate_b_count += 1

    # region 2:
    if winner(region_2_candidate_a_probability) == "Candidate A":
        region_2_candidate_a_count += 1
    else:
        region_2_candidate_b_count += 1
        
    # region 3:
    if winner(region_3_candidate_a_probability) == "Candidate A":
        region_3_candidate_a_count += 1
    else:
        region_3_candidate_b_count += 1
print()
print()
# initialize winner flags:
candidate_a_won_region_1 = False
candidate_a_won_region_2 = False
candidate_a_won_region_3 = False


# calculate region 1 winner:
if region_1_candidate_a_count > region_1_candidate_b_count:
    candidate_a_won_region_1 = True
    print(f"Candidte A won Region 1 with a percentage of winning of\
 {(region_1_candidate_a_count / simulation_number): .0%}")
else:
    candidate_b_won_region_1 = True
    print(f"Candidte B won Region 1 with a percentage of winning of\
 {(region_1_candidate_b_count / simulation_number): .0%}")

# calculate region 2 winner:
if region_2_candidate_a_count > region_2_candidate_b_count:
    candidate_a_won_region_2 = True
    print(f"Candidte A won Region 2 with a percentage of winning of\
 {(region_2_candidate_a_count / simulation_number): .0%}")
else:
    candidate_b_won_region_2 = True
    print(f"Candidte B won Region 2 with a percentage of winning of\
 {(region_2_candidate_b_count / simulation_number): .0%}")

# calculate region 3 winner:
if region_3_candidate_a_count > region_3_candidate_b_count:
    candidate_a_won_region_3 = True
    print(f"Candidte A won Region 3 with a percentage of winning of\
 {(region_3_candidate_a_count / simulation_number): .0%}")
else:
    candidate_b_won_region_3 = True
    print(f"Candidte B won Region 3 with a percentage of winning of\
 {(region_3_candidate_b_count / simulation_number): .0%}")

candidate_a_won_elections = (candidate_a_won_region_1 and candidate_a_won_region_2) \
                            or (candidate_a_won_region_1 and candidate_a_won_region_3) \
                            or (candidate_a_won_region_2 and candidate_a_won_region_3)

if candidate_a_won_elections:
    print(f"The elections winner is: Candidate A.")
else:
    print(f"The elections winner is: Candidate B.")
