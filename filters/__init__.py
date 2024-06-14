from loader import dp
from .admin import IsAdmin, isStr


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)

