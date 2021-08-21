# Innopolis University DevOps course repository

## About The Project

This is simple Web application which shows current time in Moscow.

### Built With

*  [FastApi](https://fastapi.tiangolo.com/)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* [python3.7+](https://www.python.org/downloads/)
* [virtualenv](https://pypi.org/project/virtualenv/)
* [Docker](https://docs.docker.com/engine/install/)

## Instalation

### Using python

1. Clone this repository
   ```sh
   git clone https://github.com/KamilRizatdinov/devops.git
   ```

2. Change your current directory to devops/python_app
    ```sh
    cd devops/python_app
    ```

3. Create and activate python virtual environment
   ```sh
   python3 -m virualenv .venv
   source .venv/bin/activate
   ```

4. Install requirements
   ```sh
   pip install requirements.txt
   ```

5. Run Web application
   ```sh
   uvicorn main:app --host=0.0.0.0 --port=<port number>
   ```

### Using docker

1. Clone this repository
   ```sh
   git clone https://github.com/KamilRizatdinov/devops.git
   ```

2. Change your current directory to devops/python_app
    ```sh
    cd devops/python_app
    ```

2. Run the Web application container
    ```sh
    docker run -p <local port number>:8000 -d rizatdinov/devops_python_app
    ```

## Testing
1. Make sure you are inside devops/python_app
   ```sh
   cd devops/python_app
   ```

2. Run tests
   ```sh
   pytest .
   ```

## Usage

After successfull instalation, you should be able to open application on localhost under port number you specified (e.g. `http://localhost:<port number>`). Enjoy it!

## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Kamil Rizatdinov - k.rizatdinov@innopolis.university
