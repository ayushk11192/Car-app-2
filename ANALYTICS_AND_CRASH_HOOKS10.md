# Analytics and Crash Hooks

## Flutter
Recommended:
- `firebase_analytics`
- `firebase_crashlytics`

Track these events:
- `app_open`
- `otp_requested`
- `otp_verified`
- `vehicle_lookup_started`
- `vehicle_lookup_success`
- `vehicle_lookup_failed`
- `report_unlock_clicked`
- `payment_started`
- `payment_success`
- `payment_failed`
- `report_viewed`
- `pdf_downloaded`

## Backend
Recommended:
- structured JSON logs
- request id per request
- `/health` endpoint
- error logging with stack traces only in non-user responses

## Suggested dashboards
- DAU / WAU
- lookup success rate
- payment conversion rate
- report open rate
- crash-free sessions
