from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

def main():
    app = FastAPI()
    app.mount("/", StaticFiles(directory="src/static/", html=True))

if __name__ == "__main__":
    main()
 
 