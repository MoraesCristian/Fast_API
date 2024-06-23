from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    cliente = TestClient(app)  # ARRANGE (ORGANIZAÇÃO)

    response = cliente.get('/')  # ACT(AÇÃO)

    # ASSERT(Afirma que o status code é OK)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo'}
