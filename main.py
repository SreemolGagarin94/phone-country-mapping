from fastapi import FastAPI , Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from phone_iso3166.country import *

app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return{"access-token":form_data.username,"token-type":"bearer"}


@app.post("/get-phone-country")
async def get_phone_country(Phone_number:str, token: str = Depends(oauth_scheme)):
    country = phone_country(Phone_number)
    return {"Phone": Phone_number , "Country": country}
