FROM python:3.8

COPY requirements.txt requirements-dev.txt main.py

# Run the application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]