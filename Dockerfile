FROM python:3.8.0

EXPOSE 80
# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]