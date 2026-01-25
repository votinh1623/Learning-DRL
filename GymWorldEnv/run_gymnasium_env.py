
import gymnasium
import gymnasium_env
env = gymnasium.make('gymnasium_env/GridWorld-v0')
# import gymnasium
# import gymnasium
import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    # Tạo environment với render mode (tuỳ chọn)
    env = gymnasium.make('gymnasium_env/GridWorld-v0', 
                         render_mode="human",  # hoặc "rgb_array" hoặc None
                         size=5)  # Kích thước grid
    # Reset environment
    observation, info = env.reset()
    print(f"Observation type: {type(observation)}")
    print(f"Observation: {observation}")
    print(f"Info: {info}")
    
    # Kiểm tra không gian observation
    print(f"\n=== Observation Space ===")
    print(f"Type: {env.observation_space}")
    print(f"Sample: {env.observation_space.sample()}")
    
    # Kiểm tra không gian action
    print(f"\n=== Action Space ===")
    print(f"Type: {env.action_space}")
    print(f"Number of actions: {env.action_space.n}")
    print(f"Sample action: {env.action_space.sample()}")
    
    print(f"\n=== Running some steps ===")
    for step in range(100):
        action = env.action_space.sample()
        
        observation, reward, terminated, truncated, info = env.step(action)
        
        print(f"\nStep {step + 1}:")
        print(f"  Action: {action}")
        print(f"  Observation: {observation}")
        print(f"  Reward: {reward}")
        print(f"  Terminated: {terminated}")
        print(f"  Truncated: {truncated}")
        print(f"  Info: {info}")
        
        if terminated or truncated:
            print("  Episode ended!")
            observation, info = env.reset()
            print(f"  Reset observation: {observation}")
            break
    env.close()
    
except Exception as e:
    import traceback
    traceback.print_exc()