# Deployment and bootstrap

## 1. Run migrations
Use your normal migration flow before first boot.

## 2. Create first admin
Run:
```bash
python scripts/bootstrap_admin.py
```

## 3. Verify admin access
Use a JWT that carries the same user id as the bootstrap-created admin user.

## 4. Start retry worker
Run the retry worker on a schedule, for example every minute via cron or a queue worker beat process.

## 5. Observe
Monitor:
- audit log growth
- retry backlog
- failed webhook count
