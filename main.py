from fastapi import FastAPI

app = FastAPI()

#################################################
#조회 요청
#################################################

@app.get('/')
def home():
    return {'message' : 'Hello PlayMate'}

@app.get('/meetings')
def get_meetings():
    return {
        'meetings' : [
            {
                'id' :1,
                'name' : 'Python 스터디'
            }
        ] 
    }

@app.get('/meetings/search')
def search_meetings(category : str = 'all'):
    return {
        'category' : category,
        'message' : f"{category} 카테고리 검색"
    }

@app.get('/meetings/{meeting_id}')
def get_meetings(meeting_id: int):
    return {
        'id' :  'meeting_id',
        'name' : f'{meeting_id}번 모임'
    }

#################################################
#서버에 새 데이터 보내기
#################################################

from pydantic import BaseModel

#스키마
class MeetingCreate(BaseModel):
    name : str
    max_numbers : int


@app.post('/meetings')
def create_meeting(meeting:MeetingCreate):
    return {
        'messages' : '모임 생성을 요청받았습니다.',
        'name' : meeting.name,
        'max_numbers' : meeting.max_numbers
    }


####################################################
#특정 모임이 모집중인지 확인하는 api
####################################################

@app.get('/meetings/{meeting_id}/status')
def get_meeting_status(meeting_id : int):
    return{
        'meeting_id' : meeting_id,
        'status' : 'open'
    }

####################################################
#JSON에서 원하는 데이터 꺼내기
####################################################

@app.get('/meetings/{meeting_id}/members')
def get_meeting_members(meeting_id: int):
    return {
        'meeting_id' : meeting_id,
        'members' : [
            {
                'user_id':7,
                'nickname':'민혁',
                'discord_id' : '123456789'
            },
            {
                'user_id':8,
                'nickname':'선아',
                'discord_id' : '987654321'
            }
        ] 
    }from fastapi import FastAPI

app = FastAPI()

#################################################
#조회 요청
#################################################

@app.get('/')
def home():
    return {'message' : 'Hello PlayMate'}

@app.get('/meetings')
def get_meetings():
    return {
        'meetings' : [
            {
                'id' :1,
                'name' : 'Python 스터디'
            }
        ] 
    }

@app.get('/meetings/search')
def search_meetings(category : str = 'all'):
    return {
        'category' : category,
        'message' : f"{category} 카테고리 검색"
    }

@app.get('/meetings/{meeting_id}')
def get_meetings(meeting_id: int):
    return {
        'id' :  'meeting_id',
        'name' : f'{meeting_id}번 모임'
    }

#################################################
#서버에 새 데이터 보내기
#################################################

from pydantic import BaseModel

#스키마
class MeetingCreate(BaseModel):
    name : str
    max_numbers : int


@app.post('/meetings')
def create_meeting(meeting:MeetingCreate):
    return {
        'messages' : '모임 생성을 요청받았습니다.',
        'name' : meeting.name,
        'max_numbers' : meeting.max_numbers
    }


####################################################
#특정 모임이 모집중인지 확인하는 api
####################################################

@app.get('/meetings/{meeting_id}/status')
def get_meeting_status(meeting_id : int):
    return{
        'meeting_id' : meeting_id,
        'status' : 'open'
    }

####################################################
#JSON에서 원하는 데이터 꺼내기
####################################################

@app.get('/meetings/{meeting_id}/members')
def get_meeting_members(meeting_id: int):
    return {
        'meeting_id' : meeting_id,
        'members' : [
            {
                'user_id':7,
                'nickname':'민혁',
                'discord_id' : '123456789'
            },
            {
                'user_id':8,
                'nickname':'선아',
                'discord_id' : '987654321'
            }
        ] 
    }