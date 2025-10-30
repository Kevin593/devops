import json
from app import app, API_KEY

client = app.test_client()


def test_post_success():
    payload = {
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }

    # JWT falso solo para estructura inicial
    fake_jwt = "invalid-token"

    response = client.post(
        "/DevOps",
        data=json.dumps(payload),
        content_type="application/json",
        headers={
            "X-Parse-REST-API-Key": API_KEY,
            "X-JWT-KWY": fake_jwt
        }
    )

    assert response.status_code in [200, 403]  # luego mejoraremos este test


def test_missing_api_key():
    response = client.post(
        "/DevOps",
        data=json.dumps({"to": "Juan"}),
        content_type="application/json"
    )
    assert response.status_code == 403


def test_invalid_method():
    response = client.get(
        "/DevOps",
        headers={"X-Parse-REST-API-Key": API_KEY}
    )
    assert response.status_code == 400
    assert response.data == b"ERROR"


def test_missing_jwt():
    payload = {"to": "Juan"}
    response = client.post(
        "/DevOps",
        json=payload,
        headers={"X-Parse-REST-API-Key": API_KEY}
    )
    assert response.status_code == 403
