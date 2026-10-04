# AutoTruth Step 8

This step adds:
- Live Razorpay Flutter SDK integration scaffold
- Real provider adapter contract for India vehicle data
- Ownership checks on report access
- CI workflow for backend and Flutter checks
- Deployment manifests for Render/Railway style backend deploys
- Nginx sample config for reverse proxying

## Included

### Backend
- `app/integrations/providers/base.py`
- `app/integrations/providers/mock_provider.py`
- `app/integrations/providers/india_vehicle_provider.py`
- `app/services/report_access_service.py`
- `app/dependencies/report_guard.py`
- `app/api/routes_step8_examples.py`
- `render.yaml`
- `railway.json`
- `nginx.conf`

### Frontend
- `lib/utils/razorpay_checkout_live.dart`
- `lib/services/config_service.dart`
- `lib/services/payment_service_step8.dart`
- `lib/screens/payment_screen_step8.dart`
- `pubspec.step8.yaml`

### CI/CD
- `.github/workflows/ci.yml`

## Notes
- Razorpay plugin wiring is shown with `razorpay_flutter` package conventions.
- India provider adapter is intentionally an abstraction boundary. You should only plug in lawful, licensed sources.
- Route samples are additive examples for your Step 7 codebase, not a full replacement.
