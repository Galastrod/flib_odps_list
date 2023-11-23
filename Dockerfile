FROM python:3.9

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]