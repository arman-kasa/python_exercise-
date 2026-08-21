"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`."""
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol) or "Mocktail" (no alcohol) to `drink_name`."""
    if set(drink_ingredients) & ALCOHOLS:
        return drink_name + " Cocktail"
    return drink_name + " Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`."""
    categories = ((VEGAN, "VEGAN"),
                  (VEGETARIAN, "VEGETARIAN"),
                  (PALEO, "PALEO"),
                  (KETO, "KETO"),
                  (OMNIVORE, "OMNIVORE"))

    for category, name in categories:
        if set(dish_ingredients) <= category:
            return f"{dish_name}: {name}"


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`."""
    dish_name, dish_ingredients = dish
    return (dish_name, set(dish_ingredients) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes):
    """Create a master list of ingredients."""
    return set().union(*dishes)


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them."""
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    """Find ingredients that only appear in a single dish."""
    singletons = set()
    for dish in dishes:
        singletons ^= (dish - intersection)
    return singletons
