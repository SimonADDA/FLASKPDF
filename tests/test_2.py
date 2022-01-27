from tests.conftest import client


def test_should_return_metadata(client):
	response = client.get('/documents/1')
	data = response.data.decode() #Permet de décoder la data dans la requête
	assert data ==  "1"