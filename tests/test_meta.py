from fastapi.testclient import TestClient


def test_meta_endpoint(client: TestClient):
    """
    Test the meta endpoint returns 200 OK and correct JSON structure.
    Expected response:
    {
        "model_version": "v1.0.0",
        "input_shape": ["1", "128"]
    }
    """
    response = client.get("/api/v1/meta")
    assert response.status_code == 200
    data = response.json()
    assert "model_version" in data
    assert "input_shape" in data
    assert isinstance(data["input_shape"], list)
