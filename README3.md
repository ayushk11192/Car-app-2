# AutoTruth Step 1 Starter Kit

This is the first build step for an India-first vehicle verification app inspired by the workflow we discussed.

## What is included
- FastAPI backend starter
- Basic API routes for auth, vehicles, reports, and payments
- Mock data service for India vehicle lookup
- Flutter app shell with key screens and navigation
- Suggested repo structure for scaling into production

## Folder structure

```
autotruth_step1/
  backend/
    app/
      main.py
      routes/
      schemas/
      services/
    requirements.txt
  frontend/
    pubspec.yaml
    lib/
      main.dart
      screens/
      widgets/
```

## Backend run instructions

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend docs will be available at:
- http://127.0.0.1:8000/docs

## Frontend run instructions

```bash
cd frontend
flutter pub get
flutter run
```

## Step 1 scope
This step is intentionally focused on structure and flow, not production integrations.
For now, vehicle lookup uses mock data and fixed risk scoring.

## Suggested Step 2
- Connect a real vehicle data provider
- Add PostgreSQL models and migrations
- Add OTP service and Razorpay integration
- Replace mock report generation with persisted reports
