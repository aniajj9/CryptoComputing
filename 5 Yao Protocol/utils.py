import hmac
import hashlib


def hmac_sha256(key, message):
    return hmac.new(key.encode(), message.encode(), digestmod=hashlib.sha256).hexdigest()
    