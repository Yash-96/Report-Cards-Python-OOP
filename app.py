from generate import generate

class app(object):

    def __init__(self):
        generate_obj = generate()
        generate_obj.start()
        generate_obj.update_mark()
        generate_obj.publish()

app()
