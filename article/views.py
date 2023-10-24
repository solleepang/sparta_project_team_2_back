from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from article.models import Article
from article.serializers import ArticleSerializer


class ArticleView(APIView):
    """ 게시글 생성, 조회 """

    def get(self, request):
        """ 전체 게시물 조회 """
        article = Article.objects.all()
        serializers = ArticleSerializer(article, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ 게시물 생성 """
        # TODO: 유저앱 생성 후 수정
        # if not request.user.is_authenticated:
        #     return Response({'message':'로그인 해주세요.'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            # serializer.save(user=request.user)
            serializer.save()
            return Response({'message': '게시글이 등록되었습니다.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    """ 게시글 상세 조회, 수정, 삭제 """

    def get(self, request, article_id):
        """ 특정 게시물 조회 """
        article = get_object_or_404(Article, id=article_id)
        serializers = ArticleSerializer(article)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, article_id):
        """ 특정 게시물 수정 """
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '게시글이 수정되었습니다.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': '게시글이 수정되지 않았습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        # TODO: 유저앱 생성 시 권한 유무 확인 부분 추가
        # if request.user == article.user:
        #     serializer = ArticleSerializer(article, data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response({'message': '게시글이 수정되었습니다.'}, status=status.HTTP_200_OK)
        #     else:
        #         return Response({'message': '게시글이 수정되지 않았습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     return Response({'message':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, article_id):
        """ 게시물 삭제 """
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response({'message': '게시글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        # TODO: 유저앱 생성 시 권한 유무 확인 부분 추가
        # if request.user == article.user:
        #     article.delete()
        #     return Response({'message':'삭제 되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        # else:
        #   return Response({'message':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
