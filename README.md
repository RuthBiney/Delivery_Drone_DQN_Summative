Delivery Drone Optimization with DQN
This project demonstrates the use of Deep Q-Learning (DQN) to train a reinforcement learning agent in a custom simulated environment. The agent represents a delivery drone navigating a 5x5 grid environment to deliver a parcel to a specified destination while avoiding unnecessary movements.

Environment Overview
The environment is a 5x5 grid with the following components:

1. Drone (D): The agent controlled by the DQN model.
2. Parcel (P): The parcel the drone is tasked to deliver.
3. Destination (X): The goal for the drone.

Actions
The drone can perform the following actions:

1. Move Up
2. Move Down
3. Move Left
4. Move Right
5. Pick the parcel
6. Drop the parcel

Rewards

1. Reach Destination: +100 reward.
2. Step Penalty: -1 for every step taken.
3. Distance Penalty: Reward decreases as distance to the destination increases.

Installation

1. Step 1: Clone the Repository "https://github.com/RuthBiney/Delivery_Drone_DQN_Summative.git"
2. Step 2: Set Up Virtual Environment
   python -m venv env
   mac: source env/bin/activate On Windows: .\env\Scripts\activate
3. Step 3: Install Dependencies
   pip install gym stable-baselines3 pygame numpy
   pip install 'shimmy>=2.0'

Usage

1. Train the Model
   Run the train.py script to train the DQN agent: python train.py
2. Test the Trained Model
   Run the test_env.py script to observe the agent's performance in the console: python test_env.py
3. Play with Visualization
   Run the play.py script to visualize the agent's behavior with a Pygame-based interface: python play.py

Dependencies
The project uses the following libraries:

1. Gym: For building the custom environment.
2. Stable-Baselines3: For DQN implementation.
3. Numpy: For mathematical computations.
4. Pygame: For graphical visualization.

Install all dependencies with:
pip install -r requirements.txt

Demo

1. Console-Based Test
   The test_env.py script outputs the drone's movements and grid state to the console.
2. Graphical Simulation
   The play.py script visualizes the drone navigating the grid:

Links
youtube video: https://www.youtube.com/watch?v=gVO_ye0jKtc

simulation link: https://drive.google.com/file/d/12I2Ey4AvVhkub6t-VYOjFVtXK0mV9n_h/view?usp=sharing
