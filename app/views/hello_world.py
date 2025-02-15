from ..controllers.hello_world_controller import HelloWorldController


def hello_world():
    try:
        controller = HelloWorldController()
        result = controller.run()
    except Exception as e:
        return {'message': str(e)}, 500
    return {'message': result}, 200
