from tests.conftest import client


def test_should_status_code_ok(client):
	response = client.get('/documents')
	assert response.status_code == 200
	


def test_should_status_code_nok(client):
	response = client.get('/flask')
	assert response.status_code == 404
	

def test_should_status_code_noID(client):
	response = client.get('/documents:0')
	assert response.status_code == 404
