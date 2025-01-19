import os
import pickle
import math


class MLPlay:
    def __init__(self, *args, **kwargs):
        print("Initial ml script")

        self.search_range = 1000
        encoder_path = "dataset/knn_encoder.pkl"
        model_path = "dataset/knn_model.pkl"  # Adjust path if needed
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")

        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
        if not os.path.exists(encoder_path):
            raise FileNotFoundError(
                f"Encoder file not found at {encoder_path}")
        with open(encoder_path, "rb") as f:
            self.encoder = pickle.load(f)

    def update(self, scene_info: dict, *args, **kwargs):
        """
        Generate the command according to the received scene information
        """
        score_vector = [5, 0, 0, 0]  # score for [up, down, left, right]

        # Feature vector must match training format
        X = [score_vector[0], score_vector[1],
             score_vector[2], score_vector[3]]

        # Predict the numeric label
        pred_label = self.model.predict([X])[0]

        # Convert numeric label back to command if using encoder
        action = self.encoder.inverse_transform([pred_label])[0]

        return [action]  # Return as a list, e.g., ["UP"]

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass

    def get_distance(self, x1, y1, x2, y2):
        """
        Calculate the distance between two points
        """
        return ((x1-x2)**2 + (y1-y2)**2)**0.5
