import os

for i in range(1, 11):
    directory_name = f"chatp{i}"
    os.makedirs(directory_name, exist_ok=True)
    os.create
    print(f"Directory '{directory_name}' created.")