# 1. Base Image: Start with a lightweight version of Python and Linux
FROM python:3.10-slim

# 2. Working Directory: Create a folder inside the container to hold our code
WORKDIR /code

# 3. Dependencies: Copy the requirements file FIRST (this makes building faster later)
COPY ./requirements.txt /code/requirements.txt

# 4. Install: Tell the container to install the libraries
RUN pip install --no-cache-dir -r /code/requirements.txt

# 5. Copy Code: Copy all of your actual app code into the container
COPY ./app /code/app

# 6. Expose Port: Tell Docker this container talks on port 8000
EXPOSE 8000

# 7. Start Command: The exact terminal command to start Uvicorn when the container wakes up
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]