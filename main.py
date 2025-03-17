from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from get_response import get_response

# Initialize the FastAPI app
app = FastAPI(docs_url=None, redoc_url=None)

#Define the request model for the policy bot endpoint
class QueryInput1(BaseModel):
    input: str
    history: str =""


# defining endpoint 
@app.post("/v1/api/policy_bot", response_class=JSONResponse)
async def generate_response(input_data: QueryInput1, request: Request):
    
    try:
        response = get_response(query=input_data.input,history=input_data.history) # using get_response function from get_response file
        
        return {"sender": "bot","response": response.content} # return the dictionary with response key have the actual fonal answer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) # if  get_response doesnt work it will give error.
    


