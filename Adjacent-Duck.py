import random

# Return the squared distance between two ducks at (x1, y1) and (x2, y2).
def distance_squared(first_duck, second_duck):
    x_difference = first_duck[0] - second_duck[0]
    y_difference = first_duck[1] - second_duck[1]
    return x_difference * x_difference + y_difference * y_difference


def find_nearest_duck(reference_duck, ducks):
    nearest_duck = None
    nearest_distance_squared = float("inf")
    # float("inf") = positive infinity

    for candidate_duck in ducks:
        if candidate_duck == reference_duck:
            continue

        candidate_distance_squared = distance_squared(reference_duck, candidate_duck)
        if candidate_distance_squared < nearest_distance_squared:
            nearest_duck = candidate_duck
            nearest_distance_squared = candidate_distance_squared

    return nearest_duck


def run_trial(rng, other_duck_count):
    duck_a = (0.5, 0.5)
    ducks = [duck_a]
    for duck_number in range(other_duck_count):
        x_position = rng.random()
        y_position = rng.random()
        ducks.append((x_position, y_position))

    duck_b = find_nearest_duck(duck_a, ducks)
    nearest_to_b = find_nearest_duck(duck_b, ducks)
    return nearest_to_b == duck_a


if __name__ == "__main__":
    rng = random.Random(40)
    trial_count = 100_000
    successful_trials = 0
    other_duck_count = 1000

    for trial_number in range(trial_count):
        if run_trial(rng, other_duck_count) == True:
            successful_trials += 1

    estimated_probability = successful_trials / trial_count
    print(f"Mutual nearest neighbors in {successful_trials:,} out of {trial_count:,} trials.")
    print(f"Estimated probability: {estimated_probability:.2%}")