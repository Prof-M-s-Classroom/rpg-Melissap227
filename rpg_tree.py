class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        print(f"TODO: Initialize StoryNode with event_number={event_number}, description={description}")
        # TODO: Initialize instance variables (event_number, description, left, right)

        self.event_number = event_number #keys
        self.description = description
        self.left = left #choice 1
        self.right = right #choice 2

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):
        print("TODO: Initialize an empty decision tree")
        # TODO: Initialize an empty dictionary to store nodes
        # TODO: Set root to None

        self.nodes = {}  #dictionary to store StoryNode objects (values)
        self.root = None

    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""
        print(f"TODO: Insert event {event_number} with description '{description}' into the tree")
        # TODO: Check if event_number exists in self.nodes, if not create a new StoryNode
        if(event_number not in self.nodes):
            self.nodes[event_number] = StoryNode(event_number, description, left_event, right_event)
        # TODO: Assign left and right children based on left_event and right_event
        self.nodes[event_number].left = self.nodes.get(left_event)  #safely checks left and right event nodes in "nodes"
        self.nodes[event_number].right = self.nodes.get(right_event)

        # TODO: Set root if it's the first node inserted
        if(self.root is None):
            self.root = self.nodes[event_number]

    def play_game(self):
        """Interactive function that plays the RPG."""
        print("TODO: Implement the game logic for traversing the decision tree")
        # TODO: Start from the root node
        node = self.root
        # TODO: Loop through player choices, navigating left or right based on input
        # TODO: Print event descriptions and ask for player decisions
        # TODO: End game when reaching a leaf node (where left and right are None)
        
        while node.left is not None or node.right is not None:
            print(f"Current event: {node.description}")
            choice = input("Enter 1 or 2 to make a choice:")
            if choice == "1" and node.left:
                node = node.left
            elif choice == "2" and node.right:
                node = node.right
            else:
                print("Invalid choice. Enter 1 or 2")

        print(f"Game over. Final event: {node.description}")

def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    print(f"TODO: Read story file '{filename}' and parse events")
    # TODO: Open the file and read line by line
    # TODO: Split each line into event_number, description, left_event, right_event
    # TODO: Call game_tree.insert() for each event to build the tree
    try: 
        with open(filename, "r") as file:
            for line in file:
                parts = [part.strip() for part in line.split("|")]

                event_number = int(parts[0])
                description = parts[1]
                left_event = int(parts[2]) if parts[2].lower() != 'none' else None
                right_event = int(parts[3]) if parts[3].lower() != 'none' else None
                game_tree.insert(event_number, description, left_event, right_event)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


# Main program
if __name__ == "__main__":
    print("TODO: Initialize the GameDecisionTree and load story data")
    game_tree = GameDecisionTree()

    print("TODO: Load the story from 'story.txt'")
    load_story("story.txt", game_tree)

    print("TODO: Start the RPG game")
    game_tree.play_game()