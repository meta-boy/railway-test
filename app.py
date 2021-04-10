import uvicorn
import os

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=int(os.getenv('PORT', '5000')), log_level="info", reload=True)
