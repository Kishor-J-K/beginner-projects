
story = """
In the forgotten realm of <Land>, where <Color>-green <Landmarks> whispered secrets and <Age>-old ruins held untold mysteries, a <Adjective> wanderer named <Name> set out on a quest. Legends spoke of a hidden sanctuary, guarded by the elusive Moonlight Guardians, where a wish could be granted under the light of the Silver Moon.

Guided by a mystical map passed down through generations, <Name> journeyed through <Terrain> thickets and crossed babbling <Water Features>. Along the way, a mischievous <Mythical Creature> named <Companion> joined as a spirited companion, drawn by the allure of adventure.

As <Name> and <Companion> approached the Moonlit Sanctuary, they encountered a series of riddles carved into the <Vegetation>. With <Trait> and courage, they solved each puzzle, earning the respect of the enigmatic Moonlight Guardians.

Beneath the radiant Silver Moon, <Name> made a heartfelt wish, a desire to bring a touch of magic to the ordinary lives of <Inhabitants>. The Moonlight Guardians, pleased by the selfless request, granted <Name> a vial of Stardust, a magical substance that could make dreams come true.

<Name> returned to the villages of <Land>, sprinkling Stardust to transform mundane objects into enchanting wonders. <Flowers> bloomed with vibrant hues, and ordinary stones shimmered with ethereal glow. The once-dull world became a tapestry of magic and joy.

<Companion>, having found a sense of purpose, soared into the skies, leaving trails of radiant feathers that brought smiles to those who discovered them. <Name>, content with the newfound enchantment in <Land>, continued to wander, knowing that the magic of the Moonlit Sanctuary had touched the hearts of all who called the realm home.

And so, the tale of <Name> and <Companion> became a whispered legend, inspiring wanderers to seek the hidden wonders that awaited beneath the Silver Moon in the mystical realm of <Land>.
"""

# Ask the user for words to fill in the blanks
Land = input("Enter a Mythical place name: ")
Color = input("Enter a Color: ")
Landmarks = input("Enter a Landmark like \"sea,mountain\": ")
Age = input("Enter an Age: ")
Adjective = input("Enter an Adjective: ")
Name = input("Enter a name: ")
Terrain = "dense"
Water_Features = input("Enter a water feature like \"hot water\": ")
Mythical_Creature = input("Enter a Mythical creature: ")
Companion = input("Enter a Companion: ")
Vegetation = input("Enter a Vegetation: ")
Trait = input("Enter a Trait: ")
Inhabitants = f"{Land}'s"
Flower = input("Enter a Flower: ")

# Replace placeholders with user-inputted words
filled_story = story.replace("<Land>", Land)
filled_story = filled_story.replace("<Companion>", Companion)
filled_story = filled_story.replace("<Vegetation>", Vegetation)
filled_story = filled_story.replace("<Flower>", Flower)
filled_story = filled_story.replace("<Inhabitants>", Inhabitants)
filled_story = filled_story.replace("<Trait>", Trait)
filled_story = filled_story.replace("<Color>", Color)
filled_story = filled_story.replace("<Landmarks>", Landmarks)
filled_story = filled_story.replace("<Age>", Age)
filled_story = filled_story.replace("<Adjective>", Adjective)
filled_story = filled_story.replace("<Name>", Name)
filled_story = filled_story.replace("<Terrain>", Terrain)
filled_story = filled_story.replace("<Water Features>", Water_Features)
filled_story = filled_story.replace("<Mythical Creature>", Mythical_Creature)

# Print the completed story
print("\nYour Mad Libs Story:\n")
print(filled_story)