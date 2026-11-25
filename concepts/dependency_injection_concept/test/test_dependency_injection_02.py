from fastapi.testclient import TestClient

from concepts.dependency_injection_concept.dependency_injection_02 import get_db_session ,app
# from dependency_injection_02 import app, get_db_session
# from dependency_injection_concept.dependency_injection_02 import app, get_db_session


testing_db = ["Test db for testing"]

def get_testing_db():
    return testing_db

app.dependency_overrides[get_db_session] = get_testing_db
client = TestClient(app)

def test_add_item():
    response = client.post("/items/?item=sugar")
    # print(response)
    assert response.status_code == 200
    assert response.text == '{"message":"Added item sugar","status_code":201}'