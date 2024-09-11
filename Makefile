install:
	pip install --no-cache-dir -r requirements.txt
parallel:
	python -m PyInstaller --onefile lib/parallel_threads.py
	cp ./sleep_data_large.csv ./dist/sleep_data_large.csv
concurrent:
	python -m PyInstaller --onefile lib/concurrent_threads.py
	cp ./sleep_data_large.csv ./dist/sleep_data_large.csv
docker-build-parallel:
	docker build -f Dockerfile.parallel -t parallel .
docker-run-parallel:
	docker run -it --rm --name parallel parallel
docker-build-concurrent:
	docker build -f Dockerfile.concurrent -t concurrent .
docker-run-concurrent:
	docker run -it --rm --name concurrent concurrent