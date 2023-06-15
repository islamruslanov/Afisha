from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorSerializers,MoviesSerializers,ReviewSerializer
from .models import Director,Movie,Review


@api_view(["GET"])
def director_list_api_view(request):
    director = Director.objects.all()
    data = DirectorSerializers(instance=director,many=True).data
    return Response(data=data)

@api_view(["GET"])
def director_item_api_view(request,id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'Director not found!!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializers(director,many=False).data
    return Response(data=data)

@api_view(['GET'])
def movies_list_api_view(request):
    movie = Movie.objects.all()
    data = MoviesSerializers(instance=movie,many=True).data
    return Response(data=data)

@api_view(["GET"])
def movies_item_api_view(request,id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'Movie not found'},
                        status=status.HTTP_204_NO_CONTENT)
    data = MoviesSerializers(movie,many=False).data
    return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(instance=review,many=True).data
    return Response(data=data)

@api_view(["GET"])
def review_item_api_view(request,id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'Review not found!!',
                              status.HTTP_404_NOT_FOUND})
    data = ReviewSerializer(review,many=False).data
    return Response(data=data)



@api_view(['GET'])
def test_api_view(request):
    dict_ = {
        'text' : 'hello world',
        'int' : 34,
        'bool' : True,
        'float' : 2.34,
        'list' : [1,3,"hello"],
        'dict': {
            "text" : "hii"
        }
    }
    return Response(data=dict_)

