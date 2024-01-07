import random


# Constants representing exercises and their muscle groups
EXERCISES = ['Push-up', 'Squat', 'Plank', 'Jumping Jacks', 'Lunges', 'Burpees', 'Deadlift', 'Bicep Curls']
EXERCISES_MUSCLE_GROUPS = {
    'Push-up': ['Chest', 'Shoulders', 'Triceps'],
    'Squat': ['Quadriceps', 'Hamstrings', 'Glutes'],
    'Plank': ['Core', 'Shoulders'],
    'Jumping Jacks': ['Legs', 'Cardio'],
    'Lunges': ['Quadriceps', 'Hamstrings', 'Glutes'],
    'Burpees': ['Chest', 'Legs', 'Cardio', 'Core'],
    'Deadlift': ['Lower Back', 'Glutes', 'Hamstrings'],
    'Bicep Curls': ['Biceps']
    
}


# Mapping of broader goals to muscle groups
BROADER_GOALS_TO_MUSCLE_GROUPS = {
    'lose_weight': ['Cardio'],
    'build_muscle': ['Chest', 'Quadriceps', 'Hamstrings', 'Glutes', 'Shoulders', 'Triceps', 'Core'],
    'improve_endurance': ['Cardio', 'Legs', 'Cardio'],
    'increase_flexibility': ['Core', 'Legs', 'Shoulders'],
    'total_body_fitness': ['Chest', 'Quadriceps', 'Hamstrings', 'Glutes', 'Shoulders', 'Triceps', 'Core', 'Cardio']
    

}

# Parameters for the genetic algorithm
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
NUM_GENERATIONS = 20
# Number of exercises to recommend
NUM_EXERCISES_TO_RECOMMEND = 3  # Define the number of exercises to recommend

def generate_chromosome():
    """Generate a random binary chromosome representing exercise selection."""
    return [random.choice([0, 1]) for _ in range(len(EXERCISES))]

def fitness(chromosome, user_goals, health_conditions):
    """Fitness function based on user preferences, goals, and health conditions."""
    # Count the number of desired muscle groups targeted
    targeted_muscle_groups = []
    for i in range(len(EXERCISES)):
        if chromosome[i] == 1:
            targeted_muscle_groups.extend(EXERCISES_MUSCLE_GROUPS[EXERCISES[i]])

    # Count the number of muscle groups aligned with the user's broader goals
    targeted_desired_muscle_groups = sum(
        1 for muscle_group in targeted_muscle_groups if muscle_group in user_goals)

    # Consider health conditions in fitness calculation
    # You can add specific logic based on health conditions here

    return targeted_desired_muscle_groups

def get_user_goals():
    """Get user's exercise goals and health conditions as input."""
    print("Please choose your exercise goal:")
    print("1. Lose Weight")
    print("2. Build Muscle")
    print("3. Improve_endurance")
    print("4. Increase_flexibility")
    print("5. Total_body_fitness")
    choice = input("Enter your choice : ")

    if choice == '1':
        user_goals = BROADER_GOALS_TO_MUSCLE_GROUPS['lose_weight']
    elif choice == '2':
        user_goals = BROADER_GOALS_TO_MUSCLE_GROUPS['build_muscle']
    elif choice == '3':
        user_goals = BROADER_GOALS_TO_MUSCLE_GROUPS['improve_endurance']
    elif choice == '4':
        user_goals = BROADER_GOALS_TO_MUSCLE_GROUPS['increase_flexibility']
    elif choice == '5':
        user_goals = BROADER_GOALS_TO_MUSCLE_GROUPS['total_body_fitness']
    else:
        print("Invalid choice. Using default goal: Lose Weight")
        user_goals = BROADER_GOALS_TO_MUSCLE_GROUPS['lose_weight']

    # Get user's health conditions
    health_conditions = input("Please enter your health conditions (comma-separated, e.g., Diabetes,High Blood Pressure): ").strip().split(',')
    health_conditions = [condition.strip() for condition in health_conditions]

    return user_goals, health_conditions

def genetic_algorithm(user_goals, health_conditions):
    """Genetic algorithm to recommend exercises based on user goals and health conditions."""
    # Initialize the population
    population = [generate_chromosome() for _ in range(POPULATION_SIZE)]

    for generation in range(NUM_GENERATIONS):
        # Evaluate fitness of each chromosome
        fitness_scores = [fitness(chromosome, user_goals, health_conditions) for chromosome in population]

        # Rest of the genetic algorithm steps remain the same
        # Recommend the best set of exercises
        best_chromosome = population[fitness_scores.index(max(fitness_scores))]
        recommended_exercises = [EXERCISES[i] for i in range(len(EXERCISES)) if best_chromosome[i]]
        return recommended_exercises
# Rest of the code remains unchanged

if __name__ == "__main__":
    # Get user's exercise goals and health conditions
    user_goals, health_conditions = get_user_goals()

    # Run genetic algorithm to recommend exercises
    recommended_exercises = genetic_algorithm(user_goals, health_conditions)
    if recommended_exercises:
        print('Recommended Exercises:', recommended_exercises[:NUM_EXERCISES_TO_RECOMMEND])
    else:
        print('No exercises recommended.')