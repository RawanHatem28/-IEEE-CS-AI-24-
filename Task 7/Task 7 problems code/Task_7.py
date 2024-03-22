# problem 1
def calculate_probability_distribution(data):
    total_values = len(data)
    distribution = {}

    # Count occurrences of each value
    value_counts = {}
    for value in data:
        value_counts[value] = value_counts.get(value, 0) + 1

    # Calculate probability distribution
    for value, count in value_counts.items():
        probability = count / total_values
        distribution[value] = probability

    return distribution

# problem 2
def conditional_probability(event_a, event_b):
    # Count occurrences of event A and B both occurring
    total_a_and_b = sum(1 for x, y in zip(event_a, event_b) if x == 1 and y == 1)

    # Count occurrences of event A
    total_a = event_a.count(1)

    # Calculate conditional probability
    if total_a != 0:
        probability_b_given_a = total_a_and_b / total_a
        return probability_b_given_a
    else:
        return "Event A never occurs, conditional probability undefined."

# problem 3
def bayes_theorem(prior_a, prior_b, conditional_b_given_a):
    # Calculate the denominator (P(B))
    prior_not_a = 1 - prior_a
    prior_not_b = 1 - prior_b
    denominator = (prior_a * conditional_b_given_a) + (prior_not_a * (1 - conditional_b_given_a))

    # Calculate the conditional probability of A given B using Bayes' theorem
    probability_a_given_b = (prior_a * conditional_b_given_a) / denominator
    return probability_a_given_b
