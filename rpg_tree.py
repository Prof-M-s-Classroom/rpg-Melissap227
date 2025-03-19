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
        self.left = self.nodes[left_event]
        self.right = self.nodes[right_event]
        # TODO: Set root if it's the first node inserted
        if(self.root is None):
            self.root = self.nodes[event_number]

    def play_game(self):
        """Interactive function that plays the RPG."""
        print("TODO: Implement the game logic for traversing the decision tree")
        # TODO: Start from the root node
        node = self.root
        # TODO: Loop through player choices, navigating left or right based on input
        while(node.left is not None or node.right is not None):
            print(f"Current event: {node.description}")


        # TODO: Print event descriptions and ask for player decisions
        # TODO: End game when reaching a leaf node (where left and right are None)

def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    print(f"TODO: Read story file '{filename}' and parse events")
    # TODO: Open the file and read line by line
    # TODO: Split each line into event_number, description, left_event, right_event
    # TODO: Call game_tree.insert() for each event to build the tree

# Main program
if __name__ == "__main__":
    print("TODO: Initialize the GameDecisionTree and load story data")
    game_tree = GameDecisionTree()

    print("TODO: Load the story from 'story.txt'")
    load_story("story.txt", game_tree)

    print("TODO: Start the RPG game")
    game_tree.play_game()