from django import forms


class LocationSubscribeForm(forms.Form):
    choices = [
        (1, "서울"),
        (3, "남해"),
        (4, "경기도"),
        (5, "인천"),
        (6, "제주"),
        (7, "강원도"),
        (8, "충북"),
        (9, "경북"),
        (10, "경남"),
        (11, "전북"),
        (12, "대구"),
        (13, "대전"),
        (14, "부산"),
        (15, "울산"),
        (16, "세종"),                     
    ]
    checkbox_field = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=choices,
    )
