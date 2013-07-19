
class IntroController(object):

    def __init__(self):
        self.intro_images = ['1.png', '2.png', '3.png', ]
        self.actual = 0



    def draw_image(self):

        pass

    def next(self):
        if len(self.intro_images) != 3:
            yield self.intro_images[self.actual]
        else:
            raise StopIteration()

