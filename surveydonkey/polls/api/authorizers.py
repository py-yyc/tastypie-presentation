import random
from tastypie.authorization import Authorization


class CrazyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        """
        Authorize the read of items whose description contains the user's username
        """
        username = bundle.request.user.username
        return object_list.filter(description__contains=username)

    def read_detail(self, object_list, bundle):
        """
        Authorize the read of an item based on random chance.
        """
        return random.randint(1, 2) % 2 == 0