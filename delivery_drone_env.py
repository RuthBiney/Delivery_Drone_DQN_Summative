import gym
from gym import spaces
import numpy as np


class DeliveryDroneEnv(gym.Env):
    """
    Custom Environment for a delivery drone in a 5x5 grid.
    """
    def __init__(self):
        super(DeliveryDroneEnv, self).__init__()
        self.action_space = spaces.Discrete(6)  # [Up, Down, Left, Right, Pick, Drop]
        self.observation_space = spaces.Box(low=0, high=4, shape=(6,), dtype=np.int32)  # Grid state

        # Maximum steps in an episode to prevent infinite loops
        self.max_steps = 50
        self.step_count = 0

        self.reset()

    def reset(self):
        """
        Reset the environment to its initial state.
        """
        self.drone_position = np.array([0, 0])
        self.parcel_position = np.array([2, 2])
        self.destination_position = np.array([4, 4])
        self.step_count = 0
        self.done = False
        return self._get_observation()

    def _get_observation(self):
        """
        Combine drone, parcel, and destination positions into a single observation array.
        """
        return np.concatenate((self.drone_position, self.parcel_position, self.destination_position))

    def step(self, action):
        """
        Perform an action in the environment.
        """
        # Debug action and position before applying the action
        print(f"Step {self.step_count}: Drone Position: {self.drone_position}, Action: {action}")

        # Update drone position based on action
        if action == 0:  # Move Up
            self.drone_position[1] = min(4, self.drone_position[1] + 1)
        elif action == 1:  # Move Down
            self.drone_position[1] = max(0, self.drone_position[1] - 1)
        elif action == 2:  # Move Left
            self.drone_position[0] = max(0, self.drone_position[0] - 1)
        elif action == 3:  # Move Right
            self.drone_position[0] = min(4, self.drone_position[0] + 1)

        # Increment step count
        self.step_count += 1

        # Calculate reward
        distance = np.linalg.norm(self.drone_position - self.destination_position)
        reward = -1  # Penalize every step to encourage efficiency
        if np.array_equal(self.drone_position, self.destination_position):
            reward = 100  # Reward for reaching the destination
            self.done = True
        else:
            # Penalize based on the distance to the destination
            reward -= distance / 10

        # End episode if the maximum step limit is reached
        if self.step_count >= self.max_steps:
            self.done = True

        # Debug new state and reward
        print(f"Step {self.step_count}: New Position: {self.drone_position}, Reward: {reward}")

        return self._get_observation(), reward, self.done, {}

    def render(self, mode='human'):
        """
        Render the environment in a text-based grid.
        """
        grid = np.full((5, 5), '-', dtype=str)
        grid[self.drone_position[1], self.drone_position[0]] = 'D'  # Drone
        grid[self.parcel_position[1], self.parcel_position[0]] = 'P'  # Parcel
        grid[self.destination_position[1], self.destination_position[0]] = 'X'  # Destination
        print("\n".join([" ".join(row) for row in grid]))
