# CICD-2 Two FastAPI Microservices with HTTPX

---

## Lab 5 - Two FastAPI Microservices with HTTPX

---

## Instructions

To launch service 1: 
 - Open Terminal 1 and run: 
    - python -m uvicorn product_service.main:app --host 0.0.0.0 --port 8001 --reload

To launch service 2: 
 - Open Terminal 2 and run: 
    - python -m uvicorn product_service.main:app --host 0.0.0.0 --port 8000 --reload

When the service opens, add /docs to the URL to view the pages

To test the GET endpoint, click 'Try it out' and then enter the ID of the product you are looking to GET

PRODUCT_SERVICE_URL allows the application to be flexible, when running locally it defaults to the URL specified at PRODUCT_SERVICE_URL