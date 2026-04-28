# Crear entorno virtual

```bash
cd backend
python -m venv .venv
soruce .venv/bin/activate
python -m pip install --upgrade pip
pip install "fastapi[standard]"
pip freeze > requirements.txt
```