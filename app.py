# server.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse

PCAP_FILE = "synthetic_flows1.pcap"

app = FastAPI()

# Allow JS from any origin to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def serve_html():
    try:
        # Open with utf-8 encoding to avoid UnicodeDecodeError
        with open("./templates/index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content)
    except Exception as e:
        return HTMLResponse(content=f"<h1>Error loading HTML: {e}</h1>", status_code=500)

@app.get("/get_flows")
async def get_flows():
    flows = []
    try:
        with open(PCAP_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip().strip(",").strip("[]")
            if not line:
                continue
            features = [float(x.strip()) for x in line.split(",")]
            flows.append(features)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
    return flows

@app.post("/predict")
async def predict(request: Request):
    """
    Mock prediction endpoint.
    Replace this with your actual ML model inference.
    """
    try:
        data = await request.json()
        features = data.get("features", [])

        # Mock attack probability logic (replace with ML model)
        attack_prob = sum(features) % 1000 / 1000  # just a fake probability
        label = "attack" if attack_prob > 0.5 else "normal"

        return {"label": label, "attack_probability": attack_prob}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
