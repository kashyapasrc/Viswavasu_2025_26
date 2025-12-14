import os

folder = "."  # current folder
for filename in os.listdir(folder):
    if filename.startswith("Split PDF Output-page") and filename.endswith(".pdf"):
        new_name = filename.replace("Split PDF Output-", "")
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        print(f'Renamed: {filename} -> {new_name}')
