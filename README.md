How to run this project

1. Install Flask
   pip install -r requirements.txt

2. Run the server
   python app.py

3. The server will start at:
   http://localhost:5000

4. Example endpoints
   http://localhost:5000/add?a=5&b=3
   http://localhost:5000/subtract?a=5&b=3
   http://localhost:5000/multiply?a=5&b=3
   http://localhost:5000/divide?a=5&b=3

5. Each endpoint returns a JSON result like:
   {
     "a": 5,
     "b": 3,
     "operation": "addition",
     "result": 8
   }
