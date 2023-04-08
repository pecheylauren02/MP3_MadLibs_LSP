# Define the list of story titles
story_titles = ["A Peculiar Adventure", "A Strange Fairytale", "A Day at the Office", 
                "One Summer Vacation", "A Scary Encounter", "A Day at the Beach", 
                "My First Day at School", "A Wild Party"]

# Print the list of story titles for the user to see
print("Please select a story by entering the corresponding number:")
for i, title in enumerate(story_titles):
    print(f"{i+1}. {title}")

# Ask the user to select a story
selected_story_index = int(input("Enter the number of the story you'd like to read: ")) - 1

# Retrieve the selected story title
selected_story_title = story_titles[selected_story_index]

# Print the selected story title for the user to see
print(f"You have selected the story: {selected_story_title}")
