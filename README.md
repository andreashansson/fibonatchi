# Install api
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Start API
```bash
python app/app.py
```

# Run test
```bash
cd app && python -m unittest
```

# Use the API

## Get all fibonatchi values up to given number
```bash
curl -X GET "http://localhost:5000/positions/<position>"
```

## Get fibonatchi value of given number
```bash
curl -X GET "http://localhost:5000/positions/<position>?fetch=one"
```

## Add fibonatchi position to skip
```bash
curl -X POST "http://localhost:5000/skipped" -d '{"position": "10"}' -H "Content-Type: application/json"
```

## Delete fibonatchi position from skip list
```bash
curl -X DELETE "localhost:5000/skipped/10"
```

## Get fibonatchi value of given number on skip list
```bash
curl -X GET "http://localhost:5000/positions/<position>?fetch=one"
```
example response
```json
{
    "10":"skipped"
}
```
