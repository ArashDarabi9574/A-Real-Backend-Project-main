from rest_framework.response import Response


def successful_response(data: dict, message: str = 'successful', status: int = 200):
    return Response(
        {
            'status': True,
            'message': message,
            'data': data
        },
        status=status
    )


def unsuccessful_response(data: dict, message: str = 'unsuccessful', status: int = 400) -> object:
    return Response(
        {
            'status': False,
            'message': message,
            'data': data
        },
        status=status
    )
