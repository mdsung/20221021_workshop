import pickle

with open('data/processed/data.pkl', 'rb') as f:
    results = pickle.load(f)
print(results)
