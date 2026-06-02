from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/api/metrics")
def metrics():
    return {
        "equity": 250,
        "sharpe": 1.5,
        "dd": -0.02,
        "exposure": 0.8
    }

@app.get("/api/orders")
def orders():
    return [
        {"time": "now", "symbol": "AAPL", "qty": 1, "status": "FILLED"}
    ]

@app.get("/api/risk")
def risk():
    return {
        "var": -0.02,
        "cvar": -0.05,
        "status": "OK"
    }
