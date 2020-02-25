from rest_framework.views import APIView
from rest_framework.response import Response


class homepageapi(APIView):
    """ homepage api """

    def get(self, request, format=None):
        """ list of apiview """

        homepage_api = [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        ]

        listofmenus = [
            'list of menus',
            'list of menus',
            'list of menus',
            'list of menus',
        ]

        footer = [
            'some data'
        ]

        test = ({
            'listofmenus': listofmenus,
            'body': homepage_api,
            'footer': footer
        })

        return Response(test)
