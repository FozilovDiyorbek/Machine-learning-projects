import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.monitor import Monitor
import os

env_id ="CartPole-v1"
log_dir = "Reinforcement-learning-Cartpole_DQN_Agent/logs/"
os.makedirs(log_dir, exist_ok=True)

env = gym.make(env_id, render_mode="human")
env = Monitor(env, log_dir)

policy_kwargs = dict(
    net_arch=[128, 128]  # Two hidden layer network
)

model = DQN(
    policy="MlpPolicy",
    env=env,
    learning_rate=1e-3,
    buffer_size=100000,
    learning_starts=1000,
    batch_size=64,
    gamma=0.99,
    tau=1.0,
    train_freq=4,
    target_update_interval=1000,
    exploration_fraction=0.2,
    exploration_final_eps=0.05,
    verbose=1,
    tensorboard_log=log_dir,
    policy_kwargs=policy_kwargs
)

checkpoint_callback = CheckpointCallback(
    save_freq=10000,
    save_path="Reinforcement-learning-Cartpole_DQN_Agent/checkpoints/",
    name_prefix="cartpole_dqn_model"
)

model.learn(total_timesteps=10000,
            log_interval=10,
            callback=checkpoint_callback
)

model.save("Reinforcement-learning-Cartpole_DQN_Agent/models/cartpole_dqn_final")
print("Model trained va saved!")

# Model evaluation
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
print(f"Average reward: {mean_reward:.2f} ± {std_reward:.2f}")

obs, info = env.reset()
done = False
total_reward = 0

while not done:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    done = terminated or truncated

env.close()
print(f"Hidden reward: {total_reward}")