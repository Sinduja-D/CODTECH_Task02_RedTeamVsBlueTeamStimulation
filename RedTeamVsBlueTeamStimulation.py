import random
import time

# Red Team Attack Simulation
def red_team_attack():
    target_port = random.randint(0, 65535)
    print(f"Red Team is scanning port: {target_port}")
    print("Red Team launches a phishing attack on the network.")


# Blue Team Defense Simulation
def blue_team_defense():
    print("Blue Team is monitoring network traffic for anomalies...")
    print("Blue Team detects unusual network activity.")

if __name__ == "__main__":
    print("Cybersecurity Simulation - Red Team vs Blue Team\n")
    
    # Red Team Attack
    red_team_attack()
    
    # Blue Team Defense
    blue_team_defense()