# AutoTruth Step 2 - Database-backed Starter

This version upgrades the starter into a persistent backend with SQLAlchemy models and a cleaner project structure.

## Included
- FastAPI backend with SQLite by default and PostgreSQL-ready config
- SQLAlchemy models for users, vehicles, reports, and payments
- Mock-seeded vehicle lookup persistence
- Flutter frontend shell with API integration

## Backend setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

The API starts at `http://127.0.0.1:8000`.

## Frontend setup
```bash
cd frontend
flutter pub get
flutter run
```

For Android emulator access, replace `127.0.0.1` in `lib/services/api_service.dart` with `10.0.2.2`.

## Next recommended step
- Add Alembic migrations
- Move mock data behind provider interfaces
- Add PostgreSQL locally or via Docker
- Integrate Razorpay and real data providers
