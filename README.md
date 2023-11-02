# Install api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Start API
python app/app.py

# Run test
cd app && python -m unittest

# Use the API

## Get all fibonatchi values up to given number
curl -X GET "http://localhost:5000/positions/<position>"

## Get fibonatchi value of given number
curl -X GET "http://localhost:5000/positions/<position>?fetch=one"

## Add fibonatchi position to skip
curl -X POST "http://localhost:5000/skipped" -d '{"position": 10}' -H "Content-Type: application/json"

