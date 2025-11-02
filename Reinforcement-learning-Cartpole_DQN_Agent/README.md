# CartPole DQN Agent – Reinforcement Learning Project

This project implements a **Deep Q-Network (DQN)** agent to solve the classic **CartPole-v1** environment using **Reinforcement Learning**.  
The agent is trained with `stable-baselines3` to balance a pole on a moving cart by learning optimal control policies through trial and error.

---

## Features
- Built with **Stable-Baselines3 (DQN)** and **Gymnasium**
- Custom neural network with two hidden layers (128 units each)
- Automatic **checkpoint saving** and **TensorBoard logging**
- Model evaluation with average reward tracking
- Fully reproducible and easy to extend

---

## Project Structure
```
Reinforcement-learning-Cartpole_DQN_Agent/
│
├── logs/                       # TensorBoard logs
├── checkpoints/                # Saved model checkpoints
├── models/                     # Final trained model
├── .gitignore                  # gitignore files
└── src/train_cartpole.py       # Training and evaluation script
```

---

## ⚙️ Installation
```bash
# Clone repository
git clone https://github.com/FozilovDiyorbek/Machine-learning-projects/tree/main/Reinforcement-learning-Cartpole_DQN_Agent.git
cd Reinforcement-learning-Cartpole_DQN_Agent

# Create environment and install dependencies
pip install -r requirements.txt
```

# Training
```
python src/train_cartpole.py
```

## The model will train for 10,000 timesteps and automatically save:

Checkpoints → checkpoints/

Final model → models/cartpole_dqn_final.zip

## Monitor progress using TensorBoard:
```
tensorboard --logdir=logs/
```
# 📈 Evaluation

After training, the script automatically evaluates the agent:
```
Average reward: 195.80 ± 4.25
Hidden reward: 200.0
```
## Model Architecture

Policy: MlpPolicy

Hidden layers: [128, 128]

Learning rate: 1e-3

Gamma: 0.99

Exploration ε: 0.2 → 0.05


