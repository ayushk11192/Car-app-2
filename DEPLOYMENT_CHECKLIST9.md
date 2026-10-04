# Deployment checklist

## Backend
- Set production DATABASE_URL
- Set JWT_SECRET_KEY
- Set RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET
- Enable HTTPS and trusted proxy headers
- Run alembic migrations
- Configure webhook endpoint and shared secret verification
- Enable structured logs and error tracking

## Frontend
- Choose correct flavor entrypoint
- Configure API base URL
- Configure Razorpay key id
- Verify deep link / callback handling
- Test login, payment, PDF download, and logout flows

## Security
- Confirm report ownership checks
- Confirm masked personal data in previews
- Confirm rate limits on OTP and lookup endpoints
- Confirm CORS only allows intended domains

## Launch
- Upload Android bundle
- Upload iOS archive
- Test smoke flows on staging and production
- Prepare rollback version and release notes
