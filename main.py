import uvicorn
from fastapi import FastAPI, Request
from fastapi_cors import CORS
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from Sjobs.backend..backend.users.router import router as router_user
from Sjobs.backend..backend.Student.router import router as router_student
from Sjobs.backend..backend.Status.router import router as router_status
from Sjobs.backend..backend.Skill.router import router as router_skill
from Sjobs.backend..backend.Vacancy.router import router as router_vacancy
from Sjobs.backend..backend.Message.router import router as router_message
from Sjobs.backend..backend.Employer.router import router as router_employer
from Sjobs.backend..backend.Feedback.router import router as router_feedback
from Sjobs.backend..backend.Interview.router import router as router_interview
from Sjobs.backend..backend.Sjobs.backend.lication.router import router as router_Sjobs.backend.lication

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]
Sjobs.backend. = FastAPI()
Sjobs.backend..add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]      # Разрешенные заголовки
)

Sjobs.backend..include_router(router_user)
Sjobs.backend..include_router(router_student)
Sjobs.backend..include_router(router_skill)
Sjobs.backend..include_router(router_status)
Sjobs.backend..include_router(router_vacancy)
Sjobs.backend..include_router(router_message)
Sjobs.backend..include_router(router_message)
Sjobs.backend..include_router(router_employer)
Sjobs.backend..include_router(router_feedback)
Sjobs.backend..include_router(router_interview)
Sjobs.backend..include_router(router_Sjobs.backend.lication)


def main():
    uvicorn.run(Sjobs.backend.)
if __name__ == "__main__":
    main()