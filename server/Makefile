
run:
	clear
	python main.py

python-setup:
	@echo "python3 -m venv venv"
	@echo "pip install --upgrade pip"

# requires kaggle API key https://www.kaggle.com/docs/api
get-data:
	kaggle datasets download -d joydeb28/nlp-benchmarking-data-for-intent-and-entity
	unzip nlp-benchmarking-data-for-intent-and-entity
	# mv it into data

freeze:
	pip freeze > requirements.txt

# pip install pytest-watch
# ptw -c  -- clear
watch:
	ptw


