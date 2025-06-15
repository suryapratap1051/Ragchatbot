
## Initial Set Up
### create virtual enviroment


    ```
    $ python -m venv env
 
   ```
## activate virtual


    ```
    $ env\scripts\activate

    ```
 ## pip install 

pip install langchain sentence-transformers faiss-cpu chromadb
pip install openai fastapi uvicorn pydantic streamlit



### Run:

    ```
    $ uvicorn backend.main:app --reload
    $ streamlit run app.py
    ```
    
