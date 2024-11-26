import pygame
from stable_baselines3 import DQN
from delivery_drone_env import DeliveryDroneEnv

# Load the trained model
model = DQN.load("dqn_drone")

# Initialize the environment
env = DeliveryDroneEnv()
obs = env.reset()

# Initialize Pygame
pygame.init()
screen_size = 500
cell_size = screen_size // 5
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Delivery Drone Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DRONE_COLOR = (0, 0, 255)
PARCEL_COLOR = (255, 0, 0)
DEST_COLOR = (0, 255, 0)

# Run the simulation
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Get the agent's action
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)

    # Draw the grid
    screen.fill(WHITE)
    for x in range(5):
        for y in range(5):
            pygame.draw.rect(screen, BLACK, (x * cell_size, y * cell_size, cell_size, cell_size), 1)

    # Draw drone, parcel, and destination
    pygame.draw.rect(
        screen,
        DRONE_COLOR,
        (
            env.drone_position[0] * cell_size,
            env.drone_position[1] * cell_size,
            cell_size,
            cell_size,
        ),
    )
    pygame.draw.rect(
        screen,
        PARCEL_COLOR,
        (
            env.parcel_position[0] * cell_size,
            env.parcel_position[1] * cell_size,
            cell_size,
            cell_size,
        ),
    )
    pygame.draw.rect(
        screen,
        DEST_COLOR,
        (
            env.destination_position[0] * cell_size,
            env.destination_position[1] * cell_size,
            cell_size,
            cell_size,
        ),
    )

    pygame.display.flip()
    clock.tick(5)  # Set FPS
pygame.quit()
