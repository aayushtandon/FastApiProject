#Install the dependencies:
pip install -r requirements.txt


#Run the FastAPI server
uvicorn app.main:app --reload


#Run the tests:
pytest