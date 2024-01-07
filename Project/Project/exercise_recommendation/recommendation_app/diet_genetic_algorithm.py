import random

# Define foods and their nutritional components
FOODS = {
    'Oatmeal': {'Calories': 150, 'Protein': 5, 'Carbs': 25, 'Fat': 2, 'Type': 'Vegetarian'},
    'Yogurt': {'Calories': 120, 'Protein': 8, 'Carbs': 10, 'Fat': 4, 'Type': 'Vegetarian'},
    'Eggs': {'Calories': 70, 'Protein': 6, 'Carbs': 1, 'Fat': 5, 'Type': 'Non-Vegetarian'},
    'Banana': {'Calories': 105, 'Protein': 1.3, 'Carbs': 27, 'Fat': 0.4, 'Type': 'Vegetarian'},
    'Salad': {'Calories': 100, 'Protein': 5, 'Carbs': 10, 'Fat': 4, 'Type': 'Vegetarian'},
    'Chicken ': {'Calories': 165, 'Protein': 31, 'Carbs': 0, 'Fat': 3.6, 'Type': 'Non-Vegetarian'},
    'Rice': {'Calories': 205, 'Protein': 4, 'Carbs': 45, 'Fat': 1,'Type': 'Vegetarian'},
    'Pulses': {'Calories': 120, 'Protein': 4, 'Carbs': 21, 'Fat': 1.9,'Type': 'Vegetarian'},
    'Fish': {'Calories': 144, 'Protein': 15, 'Carbs': 3, 'Fat': 8,'Type': 'Non-Vegetarian'},
    'Broccoli': {'Calories': 55, 'Protein': 3.7, 'Carbs': 11.2, 'Fat': 0.6,'Type': 'Vegetarian'},
    'Sweet Potatoes': {'Calories': 180, 'Protein': 2, 'Carbs': 41, 'Fat': 0.2,'Type': 'Vegetarian'},
    'Mixed Vegetables': {'Calories': 50, 'Protein': 2, 'Carbs': 10, 'Fat': 0.5,'Type': 'Vegetarian'},
    'Spinach': {'Calories': 23, 'Protein': 2.9, 'Carbs': 3.6, 'Fat': 0.4, 'Type': 'Vegetarian'},
    'Almonds': {'Calories': 579, 'Protein': 21, 'Carbs': 22, 'Fat': 49, 'Type': 'Vegetarian'},
}

# Mapping of broader goals to nutritional components
BROADER_GOALS_TO_NUTRITION = {
    'lose_weight': {'Calories', 'Protein'},
    'build_muscle': {'Protein', 'Carbs','Calories','fat'}
    
}

# Parameters for the genetic algorithm
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
NUM_GENERATIONS = 20

# Number of foods to recommend for each meal
NUM_FOODS_TO_RECOMMEND_BREAKFAST = 2
NUM_FOODS_TO_RECOMMEND_LUNCH = 3
NUM_FOODS_TO_RECOMMEND_DINNER = 4

# Meal types
MEAL_TYPES = ['breakfast', 'lunch', 'dinner']

# Define nutritional goals for each meal
MEAL_GOALS = {
    'breakfast': {'Calories', 'Carbs'},
    'lunch': {'Calories', 'Protein', 'Carbs'},
    'dinner': {'Calories', 'Protein', 'Carbs', 'Fat'}
}

# Modify the generate_chromosome function to consider meal types and user's vegetarian preference
def generate_chromosome(user_info):
    """Generate a random binary chromosome representing food selection."""
    chromosome = {
        meal: [random.choice([0, 1]) for _ in range(len(FOODS))]
        for meal in MEAL_TYPES
    }

    # Ensure that only vegetarian foods are selected if the user is vegetarian
    if user_info['is_vegetarian']:
        for meal in MEAL_TYPES:
            for i, (food, info) in enumerate(FOODS.items()):
                if info['Type'] == 'Non-Vegetarian':
                    chromosome[meal][i] = 0  # Select vegetarian foods

    return chromosome

# Modify the fitness function to consider meal goals and user preferences
def fitness(chromosome, user_info):
    """Fitness function based on user preferences, goals, and user information."""
    total_fitness = 0

    # Loop through the chromosome to calculate the selected foods' nutritional values for each meal
    for meal in MEAL_TYPES:
        targeted_nutritional_components = {}
        for i, is_selected in enumerate(chromosome[meal]):
            if is_selected:
                food_name = list(FOODS.keys())[i]
                food_info = FOODS[food_name]
                for nutrient, value in food_info.items():
                    if nutrient != 'Type':
                        targeted_nutritional_components[nutrient] = targeted_nutritional_components.get(nutrient, 0) + value

        meal_goal = MEAL_GOALS[meal]

        # Calculate the meal's targeted nutrition score based on meal goals
        meal_nutrition_score = sum(targeted_nutritional_components.get(nutrient, 0) for nutrient in meal_goal)

        # Adjust the fitness score based on user's age, dietary preferences, etc.
        if user_info['age'] > 30:
            meal_nutrition_score *= 0.9  # Example: Reduce score for older individuals

        total_fitness += meal_nutrition_score

    return total_fitness

# Modify the genetic_algorithm function to recommend foods for each meal
def diet_genetic_algorithm(user_info):
    """Genetic algorithm to recommend foods for breakfast, lunch, and dinner based on user information."""
    population = [generate_chromosome(user_info) for _ in range(POPULATION_SIZE)]

    for generation in range(NUM_GENERATIONS):
        fitness_scores = [fitness(chromosome, user_info) for chromosome in population]

        # Implement genetic algorithm steps (selection, crossover, mutation) here

        # Find the best chromosome in the population
        best_chromosome = population[fitness_scores.index(max(fitness_scores))]

        # Optional: Store intermediate results or update user recommendations

    # Return the recommended foods for each meal from the best chromosome
    recommended_foods = {
        'breakfast': [food for i, food in enumerate(FOODS) if best_chromosome['breakfast'][i] == 1],
        'lunch': [food for i, food in enumerate(FOODS) if best_chromosome['lunch'][i] == 1],
        'dinner': [food for i, food in enumerate(FOODS) if best_chromosome['dinner'][i] == 1]
    }

    return recommended_foods

if __name__ == "__main__":
    # Get user's information
    user_info = {
        'age': int(input("Enter your age: ")),
        'weight': float(input("Enter your weight (kg): ")),
        'height': float(input("Enter your height (cm): ")),
        'allergies': input("Enter your allergies (comma-separated): ").split(','),
        'goals': input("Enter your goals (lose_weight or build_muscle): "),
        'is_vegetarian': input("Are you vegetarian? (yes or no): ").strip().lower() == 'yes'
    }

    # Run genetic algorithm to recommend foods for breakfast, lunch, and dinner
    recommended_foods = diet_genetic_algorithm(user_info)

    # Print the recommended foods for each meal
    print('Recommended Foods for Breakfast:', recommended_foods['breakfast'][:NUM_FOODS_TO_RECOMMEND_BREAKFAST])
    print('Recommended Foods for Lunch:', recommended_foods['lunch'][:NUM_FOODS_TO_RECOMMEND_LUNCH])
    print('Recommended Foods for Dinner:', recommended_foods['dinner'][:NUM_FOODS_TO_RECOMMEND_DINNER])






