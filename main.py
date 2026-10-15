from fastapi import FastAPI
from pydantic import BaseModel


##################################################
# 모임 조회
##################################################

app = FastAPI()

@app.get('/')
def home():
    return {'message':'Hello PlayMate'}

@app.get('/meetings')
def get_meetings():
    return {
        'meetings' : [
            {
                'id' : 1,
                'name' : 'python 스터디'
            }
        ]
    }

@app.get('/meetings/search')
def search_meetings(category: str ='all'):
    return {
        'category' : category,
        'message' : f'{category} 카테고리 검색'
    }

@app.get('/meetings/{meetings_id}')
def get_meetings(meetings_id:int):
    return {
        'id' : meetings_id,
        'name' : f"{meetings_id}번 모임"
    }

##################################################
# 모임 생성
##################################################
class MeetingCreate(BaseModel):
    name:str
    max_members: int

@app.post('/meetings')
def create_meeting(meeting:MeetingCreate):
    return {
        'message' : '모임 생성을 요청받았습니다',
        'name' : meeting.name,
        'max_members' : meeting.max_members
    }

##################################################
# 실습
##################################################

@app.get('/meetings/{meetings_id}/status')
def meetings_status(meetings_id:int):
    return {
        'meetings_id' :  meetings_id,
        'status' : 'open'
    }