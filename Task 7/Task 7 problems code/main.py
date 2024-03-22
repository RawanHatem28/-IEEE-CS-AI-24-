import Task_7

# input data from user to calculate probability distribution
data = input("Enter a list of values separated by spaces: ").split()
data = [int(x) for x in data]
probability_distribution = Task_7.calculate_probability_distribution(data)
print("Probability distribution:")
print(probability_distribution)

# input data from user to calculate conditional probability
event_a = input("Enter a list of 0s and 1s for event A separated by spaces: ").split()
event_a = [int(x) for x in event_a]
event_b = input("Enter a list of 0s and 1s for event B separated by spaces: ").split()
event_b = [int(x) for x in event_b]

# Calculate and print conditional probability
result = Task_7.conditional_probability(event_a, event_b)
print("Conditional probability of event B given event A:", result)

# input data from user to calculate Bayes's Theorem
prior_a = float(input("Enter the prior probability of event A: "))
prior_b = float(input("Enter the prior probability of event B: "))
conditional_b_given_a = float(input("Enter the conditional probability of event B given event A: "))

# Calculate and print the probability of event A given event B
result = Task_7.bayes_theorem(prior_a, prior_b, conditional_b_given_a)
print("Probability of event A given event B:", result)
