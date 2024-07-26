from sqlalchemy import select

from fast_api.models import User


def test_create_user(session):
    user = User(
        username='Cristian',
        email='cristian@mail.com',
        password='Cristian**123',
    )

    session.add(user)
    session.commit()
    # session.refresh(user)
    result = session.scalar(
        select(User).where(User.email == 'cristian@mail.com')
    )

    assert result.id == 1
