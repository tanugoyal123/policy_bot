from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from get_response import get_response

app = FastAPI(docs_url=None, redoc_url=None)


class QueryInput1(BaseModel):
    input: str
    history: str =""

class QueryInput2(BaseModel):
    query: str
    city_name: str 

    

@app.post("/v1/api/policy_bot", response_class=JSONResponse)
async def generate_response(input_data: QueryInput1, request: Request):
    
    try:
        response = get_response(query=input_data.input,history=input_data.history)
        
        return {"sender": "bot","response": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


