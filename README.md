# Microservice

[![Build Status](https://travis-ci.org/lucas625/Microservice.svg?branch=master)](https://travis-ci.org/lucas625/microservice) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/53eee9a1269941b5a21649919974e7bb)](https://www.codacy.com/manual/lucas625/Microservice?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lucas625/Microservice&amp;utm_campaign=Badge_Grade)

Repository for Microservice classes and project.

- [Microservice](#microservice)
  - [Team](#team)
  - [Requirements](#requirements)
  - [Guidelines](#guidelines)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
  - [Testing](#testing)
  - [Additional Topics](#additional-topics)

## Team

- Project Manager: [Lucas Aurelio](https://github.com/lucas625)
- Developer: [Lucas Thierry](https://github.com/LucasThierry)
- Developer: [Leão Liu](https://github.com/lionliu)

## Requirements

- [Pyenv](https://github.com/pyenv/pyenv)
- [Pipenv](https://github.com/pypa/pipenv)

## Guidelines

- [The Twelve-Factor App](https://12factor.net/)

## Installation

1. Git
    Download [Git](https://git-scm.com/download/win)

2. Clone the project

    ```$ git clone https://github.com/lucas625/Microservice.git```

3. Install [Pyenv](https://github.com/pyenv/pyenv)
   - If you are using windows it might be easier to just install python 3.7

4. Install [Pipenv](https://github.com/pyenv/pyenv)

5. Setup environment

    1. Go to project folder.
    2. ```$ pipenv --python 3.7```
    3. ```$ pipenv shell```
    4. ```$ pipenv install --dev```

6. Pre-commit

    ```$ pre-commit install```

## Running the Project

After installing all dependencies, follow the next steps to run the project.

1. Security

   - Add environment variables to your current terminal
        - Ubuntu

            ```sh
            export SECRET_KEY=$(python resources/scripts/get_secret_key.py)
            export ALLOWED_HOSTS=$(python resources/scripts/get_allowed_hosts.py)
            export DEBUG='True'
            ```

        - Windows

            ```sh
            set SECRET_KEY='Anything'
            set ALLOWED_HOSTS='[*]'
            set DEBUG='True'
            ```

2. Migrations

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Running the server

    ```$ python manage.py runserver```

## Testing

- Testing without coverage

    ```python manage.py test --no-input --debug-mode```

- Testing with coverage

    ```coverage run manage.py test --no-input --debug-mode -v 2```

## Additional Topics

- Linter
  - Always run pylint for all packages and files and do the necessary fixes

    ```pylint --load-plugins pylint_django package_name```
