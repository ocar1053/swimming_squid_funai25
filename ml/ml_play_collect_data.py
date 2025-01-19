import pickle
import os
import random


class MLPlay:
    def __init__(self, *args, **kwargs):

        self.search_range = 1000
        self.data = []
        self.all_data = []

        # check if the directory dataset exists
        if not os.path.exists("dataset"):
            os.makedirs("dataset")
            print("Directory 'dataset' created.")

        # check if the file training_data.pkl exists
        if os.path.exists("dataset/training_data.pkl"):
            with open("dataset/training_data.pkl", "rb") as f:
                self.all_data = pickle.load(f)
            print(
                f"Loaded existing data with {len(self.all_data)} entries.")
        else:
            print("No existing data found, starting fresh.")

        self.last_status = None

    def update(self, scene_info: dict, *args, **kwargs):
        """
        Generate the command according to the received scene information
        """

        score_vector = [5, 0, 0, 0]  # score for [up, down, left, right]

        # decide the command according to score_vector
        command = self.decide_command(score_vector)

        # collect the data
        row = [score_vector[0], score_vector[1],
               score_vector[2], score_vector[3], command[0]]
        self.data.append(row)

        self.last_status = scene_info["status"]

        # return the command to move squid
        return command

    def decide_command(self, score_vector):
        """
        Decide the command to move the squid
        """
        actions = ["UP", "DOWN", "LEFT", "RIGHT"]

        return random.sample(actions, 1)

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")

        if self.last_status == "GAME_PASS":
            self.all_data.extend(self.data)

            with open("dataset/training_data.pkl", "wb") as f:
                pickle.dump(self.all_data, f)
            print(f"Data appended, total {len(self.all_data)} entries saved.")

        self.data.clear()

    def get_distance(self, x1, y1, x2, y2):
        """
        Calculate the distance between two points
        """
        return ((x1-x2)**2 + (y1-y2)**2)**0.5
