install:
	pip install --no-cache-dir -r requirements.txt
parallel:
	python -m PyInstaller --onefile lib/parallel_threads.py
	cp ./sleep_data_large.csv ./dist/sleep_data_large.csv
concurrent:
	python -m PyInstaller --onefile lib/concurrent_threads.py
	cp ./sleep_data_large.csv ./dist/sleep_data_large.csv