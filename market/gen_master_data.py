from market.models import Market


def gen_master(apps, schema_editor):
    # 운영서버에서 테스트를 위해 임시로 허용
    # if not settings.DEBUG:
    #     return

    Market(name="언니네옷가게", site_url="https://www.abc1.co.kr", email="test1@test.com", master_id=2, description='언니네와 함께 아름다운 스타일을 완성해보세요. #오피스룩 #2030 #판교').save()
    Market(name="누나네옷가게", site_url="https://www.abc2.co.kr", email="test2@test.com", master_id=3, description='편한 스타일링을 추구합니다. #일상 #미니멀 #VLOG').save()

    market3: Market = Market(name="이모네옷가게", site_url="https://www.abc3.co.kr", email="test3@test.com", master_id=4, description='화려한 스타일을 추구합니다. #페북여신 #인스타여신')
    market3.save()

    market3.description = "화려한 스타일을 추구합니다. #인스타여신 #트위터여신"
    market3.save()