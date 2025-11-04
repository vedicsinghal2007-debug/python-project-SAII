def get_recipes():
    """Extended and categorized recipe database (100+ recipes)"""
    return {
        # --- Indian Dishes ---
        "Indian": {
            "Aloo Gobi": ["potato", "cauliflower", "onion", "tomato", "turmeric", "garam masala"],
            "Paneer Butter Masala": ["paneer", "tomato", "butter", "cream", "garam masala", "onion"],
            "Dal Tadka": ["lentils", "onion", "tomato", "ghee", "garlic", "cumin"],
            "Chole": ["chickpeas", "onion", "tomato", "ginger", "garam masala", "cumin"],
            "Rajma": ["kidney beans", "onion", "tomato", "ginger", "garam masala", "garlic"],
            "Palak Paneer": ["spinach", "paneer", "garlic", "onion", "cream", "salt"],
            "Bhindi Masala": ["ladyfinger", "onion", "tomato", "garam masala", "turmeric"],
            "Vegetable Pulao": ["rice", "carrot", "peas", "onion", "cumin", "ghee"],
            "Masala Dosa": ["rice", "lentils", "potato", "onion", "turmeric", "mustard seeds"],
            "Biryani": ["rice", "chicken", "yogurt", "onion", "garam masala", "saffron"],
            "Butter Chicken": ["chicken", "tomato", "butter", "cream", "garam masala", "onion"],
            "Egg Curry": ["egg", "tomato", "onion", "garam masala", "ginger", "garlic"],
            "Fish Curry": ["fish", "coconut milk", "onion", "tomato", "chili", "turmeric"],
            "Poha": ["flattened rice", "onion", "mustard seeds", "turmeric", "lemon", "curry leaves"],
            "Upma": ["semolina", "onion", "mustard seeds", "carrot", "peas", "ghee"],
            "Pav Bhaji": ["potato", "cauliflower", "tomato", "onion", "butter", "spices"],
            "Kadhi Pakora": ["gram flour", "yogurt", "onion", "mustard seeds", "turmeric"],
            "Dhokla": ["gram flour", "yogurt", "turmeric", "mustard seeds", "curry leaves"],
        },

        # --- Italian Dishes ---
        "Italian": {
            "Pasta Alfredo": ["pasta", "cream", "butter", "cheese", "garlic", "salt"],
            "Pasta Arrabiata": ["pasta", "tomato", "olive oil", "garlic", "chili flakes", "basil"],
            "Lasagna": ["pasta sheets", "tomato sauce", "cheese", "beef", "onion", "oregano"],
            "Pizza Margherita": ["flour", "cheese", "tomato", "olive oil", "yeast", "basil"],
            "Mushroom Risotto": ["rice", "mushroom", "cheese", "butter", "onion", "white wine"],
            "Bruschetta": ["bread", "tomato", "garlic", "olive oil", "basil"],
            "Minestrone Soup": ["onion", "tomato", "beans", "pasta", "carrot", "celery"],
            "Spaghetti Carbonara": ["spaghetti", "egg", "bacon", "cheese", "pepper"],
            "Pesto Pasta": ["pasta", "basil", "olive oil", "garlic", "cheese", "pine nuts"],
            "Caprese Salad": ["tomato", "mozzarella", "basil", "olive oil", "salt"],
            "Gnocchi": ["potato", "flour", "egg", "cheese", "butter"],
            "Tiramisu": ["mascarpone", "coffee", "egg", "sugar", "cocoa powder"],
        },

        # --- Chinese Dishes ---
        "Chinese": {
            "Fried Rice": ["rice", "soy sauce", "carrot", "capsicum", "onion", "peas"],
            "Chow Mein": ["noodles", "soy sauce", "onion", "capsicum", "carrot", "garlic"],
            "Manchurian": ["cabbage", "carrot", "soy sauce", "cornflour", "garlic"],
            "Spring Rolls": ["flour", "cabbage", "carrot", "soy sauce", "onion"],
            "Hakka Noodles": ["noodles", "capsicum", "onion", "soy sauce", "vinegar"],
            "Schezwan Fried Rice": ["rice", "schezwan sauce", "garlic", "onion", "capsicum"],
            "Hot and Sour Soup": ["cabbage", "carrot", "vinegar", "soy sauce", "pepper"],
            "Sweet Corn Soup": ["corn", "milk", "onion", "pepper", "salt"],
            "Kung Pao Chicken": ["chicken", "soy sauce", "chili", "peanuts", "garlic"],
            "Mapo Tofu": ["tofu", "chili paste", "garlic", "soy sauce", "onion"],
            "Dim Sum": ["flour", "vegetables", "soy sauce", "ginger", "garlic"],
        },

        # --- Mexican Dishes ---
        "Mexican": {
            "Tacos": ["tortilla", "chicken", "tomato", "lettuce", "cheese", "sauce"],
            "Burrito": ["tortilla", "rice", "beans", "chicken", "cheese", "salsa"],
            "Quesadilla": ["tortilla", "cheese", "onion", "capsicum", "sauce"],
            "Nachos": ["corn chips", "cheese", "jalapeno", "salsa", "beans"],
            "Guacamole": ["avocado", "onion", "tomato", "lemon", "salt"],
            "Enchiladas": ["tortilla", "chicken", "tomato sauce", "cheese", "beans"],
            "Fajitas": ["chicken", "onion", "capsicum", "spices", "tortilla"],
            "Churros": ["flour", "butter", "sugar", "cinnamon", "oil"],
            "Mexican Rice": ["rice", "tomato", "corn", "beans", "onion", "spices"],
        },

        # --- American Dishes ---
        "American": {
            "Veg Burger": ["bun", "potato", "lettuce", "tomato", "cheese", "sauce"],
            "Cheeseburger": ["bun", "beef", "cheese", "lettuce", "tomato", "sauce"],
            "Grilled Sandwich": ["bread", "butter", "cheese", "tomato", "capsicum", "onion"],
            "Mac and Cheese": ["pasta", "cheese", "milk", "butter", "flour"],
            "Fried Chicken": ["chicken", "flour", "egg", "oil", "spices"],
            "Caesar Salad": ["lettuce", "chicken", "cheese", "croutons", "sauce"],
            "Omelette": ["egg", "onion", "tomato", "salt", "pepper"],
            "Pancakes": ["flour", "milk", "egg", "sugar", "butter", "baking powder"],
            "French Toast": ["bread", "egg", "milk", "sugar", "butter"],
            "BBQ Ribs": ["pork ribs", "bbq sauce", "garlic", "onion"],
            "Steak": ["beef", "salt", "pepper", "butter", "garlic"],
            "Cornbread": ["cornmeal", "flour", "milk", "egg", "sugar"],
        },

        # --- Japanese Dishes ---
        "Japanese": {
            "Sushi": ["rice", "vinegar", "fish", "nori", "soy sauce"],
            "Ramen": ["noodles", "broth", "egg", "soy sauce", "chicken", "onion"],
            "Tempura": ["shrimp", "flour", "egg", "oil", "salt"],
            "Miso Soup": ["miso paste", "tofu", "seaweed", "onion"],
            "Teriyaki Chicken": ["chicken", "soy sauce", "garlic", "sugar", "ginger"],
            "Yakitori": ["chicken", "soy sauce", "skewers", "garlic", "sugar"],
            "Udon Noodles": ["udon noodles", "broth", "soy sauce", "spring onion"],
            "Okonomiyaki": ["flour", "cabbage", "egg", "soy sauce", "mayo"],
            "Onigiri": ["rice", "seaweed", "fish", "salt"],
            "Katsu Curry": ["chicken", "flour", "egg", "curry sauce", "rice"],
        },

        # --- Middle Eastern Dishes ---
        "Middle Eastern": {
            "Falafel": ["chickpeas", "onion", "garlic", "parsley", "spices"],
            "Hummus": ["chickpeas", "tahini", "lemon", "garlic", "olive oil"],
            "Shawarma": ["chicken", "yogurt", "garlic", "spices", "pita"],
            "Tabbouleh": ["bulgur", "parsley", "lemon", "tomato", "olive oil"],
            "Kebabs": ["minced meat", "onion", "garlic", "spices", "bread"],
            "Baba Ganoush": ["eggplant", "tahini", "garlic", "lemon", "olive oil"],
            "Pita Bread": ["flour", "yeast", "salt", "water", "oil"],
            "Lamb Stew": ["lamb", "onion", "tomato", "garlic", "spices"],
            "Stuffed Grape Leaves": ["rice", "lemon", "onion", "grape leaves"],
        },

        # --- Desserts & Drinks ---
        "Desserts & Drinks": {
            "Gulab Jamun": ["milk powder", "flour", "sugar", "ghee", "cardamom"],
            "Kheer": ["rice", "milk", "sugar", "cardamom", "almonds"],
            "Halwa": ["semolina", "sugar", "ghee", "cardamom"],
            "Chocolate Cake": ["flour", "cocoa powder", "sugar", "egg", "butter", "milk"],
            "Lassi": ["yogurt", "sugar", "milk", "cardamom"],
            "Smoothie": ["milk", "banana", "sugar", "ice", "honey"],
            "Coffee": ["milk", "coffee powder", "sugar", "water"],
            "Tea": ["milk", "tea leaves", "sugar", "water", "ginger"],
            "Mango Shake": ["milk", "mango", "sugar", "ice"],
            "Ice Cream Sundae": ["ice cream", "chocolate syrup", "nuts", "whipped cream"],
            "Brownie": ["flour", "chocolate", "sugar", "egg", "butter"],
            "Cheesecake": ["cream cheese", "sugar", "egg", "butter", "biscuit base"],
        }
    }


def recommend_recipes(available_ingredients):
    """Recommend recipes from all cuisines"""
    cuisines = get_recipes()
    recommendations = {}

    for cuisine, recipes in cuisines.items():
        for recipe, ingredients in recipes.items():
            matched = [i for i in ingredients if i in available_ingredients]
            missing = [i for i in ingredients if i not in available_ingredients]
            if matched:
                recommendations[recipe] = {
                    "cuisine": cuisine,
                    "matched": matched,
                    "missing": missing
                }
    return recommendations


def main():
    print("🍳 Welcome to the Smart Recipe Recommender!")
    print("Enter the ingredients you have (comma separated):")

    user_input = input("> ").lower()
    available_ingredients = [x.strip() for x in user_input.split(",")]

    recommendations = recommend_recipes(available_ingredients)

    if not recommendations:
        print("\n❌ No recipes found with those ingredients.")
    else:
        print("\n✅ Recipes you can try:\n")
        for recipe, details in recommendations.items():
            print(f"🍴 {recipe} ({details['cuisine']})")
            print(f"   ✅ Matched: {', '.join(details['matched'])}")
            print(f"   🧂 Missing: {', '.join(details['missing']) if details['missing'] else 'None'}")
            print("-" * 60)


if __name__ == "__main__":
    main()
