from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.log_routes import router as log_router

app = FastAPI(
    title="AI Log Analyzer",
    description="Backend API for analyzing log files using AI",
    version="1.0.0",
)

# CORS for frontend apps (local dev + deployed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-integrated-security-log-analyzer-100hsrv8u.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register log routes under /api/logs
app.include_router(log_router, prefix="/api/logs")

# Root route
@app.get("/")
def root():
    return {"message": "AI Log Analyzer backend is running! Use /api/logs/analyze"}

# Optional health check
@app.get("/health")
def health_check():
    return {"status": "ok"}



