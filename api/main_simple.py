from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"status": "Australian Legal AI - Cloud Version"}
@app.get("/health")
def health(): return {"status": "healthy"}
