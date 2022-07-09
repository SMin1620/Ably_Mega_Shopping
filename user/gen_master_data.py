from user.models import User


def gen_master(apps, schema_editor):
    """
    유저 더미데이터
    """

    User.objects.create_superuser(
        username='admin',
        password='admin',
        name='관리자',
        email='',
        gender=User.GenderChoices.MALE
    )

    for i in range(2, 6):
        username = f'user{i}'
        password = f'user{i}'
        name = f'이름{i}'
        email = ''
        gender = User.GenderChoices.FEMALE

        User.objects.create_user(
            username=username,
            password=password,
            name=name,
            email=email,
            gender=gender
        )