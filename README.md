# Mana CV lo? sini gw Roasting 😈

https://kangroasting.streamlit.app

### How To Use on Local?
1. Clone
2. put the OpenAI API Key at .streamlit\secrets.toml `OPENAI_API_KEY = "sk-XXXX`
3. create python virtual environtment `python -m venv .venv`
4. activate virtual environtment `.venv\Scripts\activate.bat`
5. install requirements
6. run `streamlit run main.py`


### How To Deploy on Streamlit Server
1. Put this code at top of main.py
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

2. Put this on first line of requirements.txt
`pysqlite3-binary`