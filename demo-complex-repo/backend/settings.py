# Obvious: AWS Access Key (matches AKIA... pattern)
AWS_ACCESS_KEY_ID = "AKIAEXAMPLEKEY12345678"

# Medium: 40-char token (could be AWS secret, could be other)
AWS_SECRET_ACCESS_KEY = "aZ9f+3J7bC4HkLmNopQrsTuvwxyZ0123456789ab"

# Not secret: demo password placeholder (the LLM should down-rank)
DATABASE_PASSWORD = "changeme"  # placeholder

# Looks like a Slack token (xoxb-...), but it's a fake for tests
SLACK_BOT_TOKEN = "xoxb-123456789012-ABCdefGHIjklMNopQRst"  # fake
