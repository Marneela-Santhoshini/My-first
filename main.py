from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import analyze_conversation

app = FastAPI()

class Transcript(BaseModel):
    text: str


@app.post("/stream")
def stream_text(data: Transcript):

    message = data.text.strip()

    # Ignore empty or default Swagger "string"
    if message.lower() == "string" or message == "":
        return {"message": "Please enter a valid message"}

    # Analyze only the current message
    result = analyze_conversation(message)

    return {
        "message": message,
        "analysis": result
    }
    