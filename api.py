from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os
import function

app = FastAPI()
# Đường dẫn tới file CSV
CSV_FILE = 'info.csv'
file_path = 'mess.json'

# Kiểm tra xem file CSV đã tồn tại hay chưa, nếu chưa thì tạo mới
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=['No','Name', 'Age', 'Educcation', 'Job', 'Hobby','ranking_list'])
    df.to_csv(CSV_FILE, index=False)    

# Route để nhận thông tin và lưu vào file CSV
@app.post("/post_info")
def get_info(item : dict):
    result = function.create_info(item)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8003, reload=True)