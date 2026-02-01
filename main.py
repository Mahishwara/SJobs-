import uvicorn
from fastapi import FastAPI, Request
from fastapi_cors import CORS
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.users.router import router as router_user
from backend.Student.router import router as router_student
from backend.Status.router import router as router_status
from backend.Skill.router import router as router_skill
from backend.Vacancy.router import router as router_vacancy
from backend.Message.router import router as router_message
from backend.Employer.router import router as router_employer
from backend.Feedback.router import router as router_feedback
from backend.Interview.router import router as router_interview
from backend.Application.router import router as router_application

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]      # Разрешенные заголовки
)

app.include_router(router_user)
app.include_router(router_student)
app.include_router(router_skill)
app.include_router(router_status)
app.include_router(router_vacancy)
app.include_router(router_message)
app.include_router(router_message)
app.include_router(router_employer)
app.include_router(router_feedback)
app.include_router(router_interview)
app.include_router(router_application)


def main():
    uvicorn.run(app)
if __name__ == "__main__":
    main()