import hmac
import hashlib


def get_sha256_digest(key, message):
    return hmac.new(key, message, digestmod=hashlib.sha256).hexdigest()
