FROM python:3.11

COPY requirements.txt requirements-dev.txt main.py

WORKDIR ./app/assets

# Run the application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]