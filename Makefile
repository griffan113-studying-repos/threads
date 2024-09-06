install:
	pip install --no-cache-dir -r requirements.txt
parallel:
	python -m PyInstaller --onefile lib/parallel.py
	cp ./sleep_data_large.csv ./dist/sleep_data_large.csv