
from django.http import JsonResponse


def get_object_or_404_res(obj, *args, **kwargs):
    if obj.objects.filter(**kwargs).exists():
        ob = obj.objects.get(**kwargs)
        return ob
    return {
            "message": f"{obj.__name__} matching query does not exist."
        }
    