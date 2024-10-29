FROM svizor/zoomcamp-model:3.11.5-slim

# Install pipenv
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --system --deploy

# Copy the Flask script
COPY model1.bin . 
COPY app.py . 

# Expose the port the app runs on
EXPOSE 9696

# Run the app with Waitress
CMD ["python", "-c", "from waitress import serve; from app import app; serve(app, host='0.0.0.0', port=9696)"]
