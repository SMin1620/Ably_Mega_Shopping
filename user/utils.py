from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


def validate_password12(password1, password2):
    validate_condition = [
        # lambda s: all(x.islower() or x.isupper() or x.isdigit() or (x in ['!', '@', '#', '$', '%', '^', '&', '*', '_']) for x in s),  ## 영문자 대소문자, 숫자, 특수문자(리스트)만 허용
        # lambda s: any(x.islower() or x.isupper() for x in s),  ## 영어 대소문자 필수
        # lambda s: any((x in ['!', '@', '#', '$', '%', '^', '&', '*', '_']) for x in s),  ## 특수문자 필수
        # lambda s: len(s) == len(s.replace(" ", "")),
        # lambda s: len(s) >= 6,  ## 글자수 제한
        lambda s: len(s) <= 20,  ## 글자수 제한
    ]

    for validator in validate_condition:
        if not validator(password1):
            raise serializers.ValidationError(
                _("password ValidationError")
            )

    if not password1 or not password2:
        raise serializers.ValidationError(
            _("need two password fields")
        )

    if password1 != password2:
        raise serializers.ValidationError(
            _("password fields didn't match!"))

    return password1
