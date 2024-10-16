# Nutrition Facts Calculator
This application calculates nutrition information for any recipe. 

<img width="898" alt="recipe" src="https://github.com/user-attachments/assets/881875ce-0fe0-4f85-8370-65d45b993778">

It takes user input for an ingredient, and then asks the user to provide nutritional information for that ingredient. Once all ingredients are entered, the user provides the desired serving size, and then the app provides the recipe's nutritional information per serving.

## Current Nutritional Information Calculated
- Fat
- Sodium
- Sugar
- Fiber
- Protein

## Assumptions and Limitations
Currently, this app assumes the user knows the **TOTAL** value of each ingredient's nutrients for the recipe. For example, if the recipe calls for `16oz creamy peanut butter`, the user will need to know the total amount of Fat  in 16oz of their peanut butter - meaning, you may have to look at your can and calculate how many servings you're adding to your recipe. 

In this example (as seen in the screenshot below) our jar of peanut butter is 16oz total. The values in the "Nutrition Facts" table show "per serving". We take the **Total Fat** value of 16g, and multiply it by the "**X** servings per container", and get **Fat = 224g**, the number we add into the calculator. 

<img width="361" alt="peanutbutter" src="https://github.com/user-attachments/assets/d39f0a9e-553e-494e-8481-8449c8dfc682">


*\*NOTE: These values may alarm you (e.g. "224g Fat" for peanut butter??), but remember, we divide the total number by serving size at the end, so the final numbers should be closer to expected values!*

# Example Recipe: Chocolate Covered Peanut Butter Protein Bars
## Ingredients
- 2 1/2 cups of Rolled Oats (blended into flour)
- 1/2 cup Vanilla Protein Powder
- Salt (to taste)
- 16oz Creamy Peanut Butter
- 1/2 cup Honey
- 1 Tablespoon Vanilla Extract
- 1/2 cup Mini Chocolate Chips
- 3x3.5oz Dark Chocolate Bar
- 1 Teaspoon Coconut Oil

Serving Size = 32 bars (pieces)


# Potential Improvements
1. Add Calories to calculation
2. Add ingredient amount calculation (1 cup vs 2 cups, etc)
3. Add serving size calculation (so the user doesn't have to know total amount of nutritional value per ingredient)
4. Have user enter all ingredients first, and then prompt for nutritional values based on provided ingredient list ("enter ingredients: oats, peanut butter, honey, etc", then "enter 'Fat' for 'oats': ", instead of "ingredient 1, enter nutritional value for ingredient 1")
