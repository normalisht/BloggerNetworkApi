from rest_framework import serializers


class NotEqualValidator:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, data):
        fields = tuple(data.keys())
        values = tuple(data.values())
        for index, el_1 in enumerate(values):
            for el_2 in values[index + 1:]:
                if el_1 == el_2:
                    raise serializers.ValidationError(
                        f'The fields {", ".join(fields)} must not be equal.')
