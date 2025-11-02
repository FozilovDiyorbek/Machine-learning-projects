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
git clone https://github.com/yourusername/Reinforcement-learning-Cartpole_DQN_Agent.git
cd Reinforcement-learning-Cartpole_DQN_Agent

# Create environment and install dependencies
pip install -r requirements.txt
```
