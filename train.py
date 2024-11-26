from stable_baselines3 import DQN
from delivery_drone_env import DeliveryDroneEnv

# Initialize the custom environment
env = DeliveryDroneEnv()

# Initialize the DQN model with MlpPolicy
model = DQN("MlpPolicy", env, verbose=1)

# Train the model with reduced timesteps for testing purposes
model.learn(total_timesteps=2000)  # Use fewer timesteps for faster testing

# Save the trained model
model.save("dqn_drone")
print("Model training complete and saved.")
