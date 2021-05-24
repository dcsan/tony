
VERSION=v0.1alpha2

setup-venv:
	@echo "run in your shell:\n   . '/Users/dc/tensorflow_macos_venv/bin/activate' "

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

# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/apple/tensorflow_macos/master/scripts/download_and_install.sh)"
get-tf-installer:
	curl -fsSL https://raw.githubusercontent.com/apple/tensorflow_macos/master/scripts/download_and_install.sh > bin/tf_installer.sh
	curl -fsSL https://raw.githubusercontent.com/apple/tensorflow_macos/master/scripts/install_venv.sh > bin/tf_venv.sh

	bash -c bin/tf_installer.sh

# curl -fLO https://github.com/apple/tensorflow_macos/releases/download/v0.1alpha2/tensorflow_macos-${VERSION}.tar.gz
tf-m1:
	@echo "installing ${VERSION}"
	curl -fLO https://github.com/apple/tensorflow_macos/releases/download/v0.1alpha2/tensorflow_macos-${VERSION}.tar.gz
	cd tensorflow_macos
	./install_venv.sh --prompt


freeze:
	pip freeze > requirements.txt

# pip install pytest-watch
# ptw -c  -- clear
watch:
	ptw


