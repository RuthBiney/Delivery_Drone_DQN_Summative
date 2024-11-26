from stable_baselines3 import DQN
from delivery_drone_env import DeliveryDroneEnv

# Load the trained model
model = DQN.load("dqn_drone")

# Initialize the custom environment
env = DeliveryDroneEnv()

# Reset the environment
obs = env.reset()

# Simulate the trained agent in the environment
done = False
step_count = 0

# Limit the number of steps during testing
while not done and step_count < 50:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    print(f"Step: {step_count}, Action: {action}, Reward: {reward}")
    step_count += 1
