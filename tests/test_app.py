from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # cliente = TestClient(app)  # ARRANGE (ORGANIZAÇÃO)

    response = client.get('/')  # ACT(AÇÃO)

    # ASSERT(Afirma que o status code é OK)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo'}
