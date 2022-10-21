import pickle

with open("data/raw/data.txt", 'r') as f:
    rl = f.readlines()
    results =[r.strip() for r in rl]

with open("data/processed/data.pkl", 'wb') as f:
    pickle.dump(results, f)
