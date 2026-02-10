## Setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install fastapi uvicorn[standard] black ruff
pip freeze > requirements.txt
```

## Run Server
```powershell
uvicorn tic_tac_toe.main:app --reload
```

## Format + Lint
```powershell
black .
ruff check . --fix
```