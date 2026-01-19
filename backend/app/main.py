from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.log_routes import router as log_router

app = FastAPI()

# CORS for frontend on Vite (5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
                "https://ai-integrated-security-log-analyzer-100hsrv8u.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(log_router, prefix="/api/logs")


