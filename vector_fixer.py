import pickle

with open("car_paths.pickle", "rb") as f:
    loaded_path = pickle.load(f)

for sublist in loaded_path:
    for vec3 in sublist:
        vec3.y = 0


with open("car_paths.pickle", "wb") as f:
    pickle.dump(loaded_path, f)