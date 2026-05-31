# AI Doctor Helper Backend Automation

This backend version removes the need to manually type the repeated `set ...` commands.

## Local start

From the backend folder, run:

```cmd
run_backend_auto.cmd
```

Or manually:

```cmd
..\..\.venv\Scripts\activate
python -m uvicorn app.main:app --reload
```

## Dynamic AI Service URL

The AI service URL can be updated without restarting the backend:

```http
POST /api/ai/config/url
```

Body:

```json
{
  "url": "https://xxxxx.trycloudflare.com",
  "source": "kaggle_cloudflare"
}
```

Check current config:

```http
GET /api/ai/config/url
```

Check AI health through backend:

```http
GET /api/ai/health
```

Warm up the remote model through backend:

```http
POST /api/ai/warmup
```

## Defaults now built in

The following defaults are set automatically in code:

- AI_CHAT_MODE=auto
- AI_REQUEST_TIMEOUT_SECONDS=900
- AI_CHAT_TIMEOUT_SECONDS=30
- AI_CHAT_RETRIES=2
- AI_XRAY_RESULT_POLLS=8
- AI_XRAY_RESULT_POLL_SECONDS=4
- AI_LAB_OCR_RETRIES=3
- AI_LAB_RESULT_POLLS=6
- AI_LAB_RESULT_POLL_SECONDS=5
- AI_LAB_UPLOAD_MAX_SIDE=1800
- AI_LAB_UPLOAD_JPEG_QUALITY=88
- AI_WARMUP_TIMEOUT_SECONDS=900
