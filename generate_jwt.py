import jwt
import time

JWT_SECRET = "SuperSecretKeyForDevOps"
JWT_ALGORITHM = "HS256"

def generate_token():
    payload = {
        "iat": int(time.time())
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

if __name__ == "__main__":
    token = generate_token()
    print("\n✅ JWT generado con éxito:\n")
    print(token)
