print: src/print.py\
		data/processed/data.pkl
	python src/print.py

data/processed/data.pkl: main.py\
						data/raw/data.txt
	python main.py