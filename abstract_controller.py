
class AbstractController(object):
    assets_dir = 'assets'


    def longpress(self):
        raise NotImplemented()

    def shortpress(self):
        raise NotImplemented()