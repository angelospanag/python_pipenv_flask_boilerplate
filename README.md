# python_pipenv_flask_boilerplate

## Prerequisites
* [Python 3.7.*](https://www.python.org/downloads/)
* [pipenv](https://docs.pipenv.org/)

### 1. Install Python 3 and pipenv

**MacOS (using `brew`)**

```bash
brew install python3 pipenv
```

**APT based distributions (Ubuntu/Debian)**

```bash
sudo apt install build-essential python-dev python3-pip
pip3 install pipenv awscli --user
```

You will also need to add the Python user base directory to your PATH. Put the following in your shell startup file (`.zshrc` for Zsh, `.bashrc` for Bash):
```bash
export PATH=$HOME/.local/bin:"$PATH"
```
### 2. Create a virtual environment with all necessary dependencies

From the root of the project execute:
```bash
pipenv install
```

### 3. Activate your virtual environment

From the root of the project execute:
```bash
pipenv shell
```

### 4. Create a `.env` file at the root folder of the project
```dotenv
# Application Environment can be 'development', 'qa', 'production'
ENVIRONMENT = development

# Flask entrypoint
FLASK_APP = main.py
```

## Run application

`make run`: Runs the Flask web application on port `5000` using gunicorn
