from http import HTTPStatus

from fast_api.schemas import UserPublic


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # cliente = TestClient(app)  # ARRANGE (ORGANIZAÇÃO)

    response = client.get('/')  # ACT(AÇÃO)

    # ASSERT(Afirma que o status code é OK)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo'}


def test_created_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'TestUserName',
            'password': 'Password',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'TestUserName',
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'Teste',
            'email': 'teste@teste.com',
            'password': '123',
        },
    )

    assert response.json() == {
        'id': 1,
        'username': 'Teste',
        'email': 'teste@teste.com',
    }


def test_deleted_user(client, user):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
