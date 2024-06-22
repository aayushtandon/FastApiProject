
## Project Structure

fastapi_project/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── controllers/
│ │ ├── init.py
│ │ └── addition_controller.py
│ ├── models/
│ │ ├── init.py
│ │ └── request_response_models.py
│ ├── services/
│ │ ├── init.py
│ │ └── addition_service.py
│ ├── utils/
│ │ ├── init.py
│ │ └── logger.py
│ └── tests/
│ ├── init.py
│ ├── test_addition.py
│ └── test_main.py
├── requirements.txt
└── README.md


## Installation

1. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Running the Server

Run the FastAPI server:

```sh
uvicorn app.main:app --reload


The server will be available at http://127.0.0.1:8000.


### Running the Project

1. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

2. **Run the FastAPI server**:

    ```sh
    uvicorn app.main:app --reload
    ```

3. **Run the tests**:

    ```sh
    pytest
    ```
