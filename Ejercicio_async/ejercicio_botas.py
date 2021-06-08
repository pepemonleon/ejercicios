import os

# env_var = input('Please enter environment variable name:\n')

env_var_value = input('Please enter environment variable value:\n')

os.environ["test"] = env_var_value

hi = os.environ["test"]

print(hi)
