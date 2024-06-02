#!/bin/bash

# Check if we're already in a virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Not currently in a virtual environment."

    # Check if the venv directory exists
    if [ -d "venv" ]; then
        echo "Found existing virtual environment. Activating..."
        source venv/bin/activate
    else
        echo "No virtual environment found. Creating one..."
        python3 -m venv venv
        echo "Virtual environment created. Activating..."
        source venv/bin/activate
        echo "Installing dependencies from requirements.txt..."
        pip3 install -r requirements.txt
    fi
else
    echo "Already in a virtual environment."
fi

# Run the application
echo "Running assistant.py..."
python3 assistant.py

