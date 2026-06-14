FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /code

# Copy requirements first to leverage Docker cache
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Create a non-root user for security (Hugging Face requires this for custom ports)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Set working directory for the user's files
WORKDIR $HOME/app

# Copy all your repository files (including app.py) into the active path
COPY --chown=user . $HOME/app

# Clear entrypoints and run Streamlit strictly with flags
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]
