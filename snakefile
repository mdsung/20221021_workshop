rule create_data_pkl:
    input:
        script="main.py",
        data="data/raw/data.txt"
    output:
        "data/processed/data.pkl"
    shell:
        "python {input.script}"
	