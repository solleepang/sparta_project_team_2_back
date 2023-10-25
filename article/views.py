from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from article.models import Article
from article.serializers import ArticleSerializer

from user.models import User


class ArticleView(APIView):
    """ 게시글 생성, 조회 """

    def get(self, request):
        """ 전체 게시물 조회 """
        article = Article.objects.all()
        serializers = ArticleSerializer(article, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ 게시물 생성 """
        if not request.user.is_authenticated:
            return Response({'message':'로그인 해주세요.'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author_id=request.user)
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
        if request.user == article.author_id:
            serializer = ArticleSerializer(article, data=request.data)
            # 작성자가 수정할 때       
            if serializer.is_valid():
                serializer.save()
                return Response({'message': '게시글이 수정되었습니다.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': '게시글이 수정되지 않았습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                # 작성자 이외의 사람의 요청이지만 이미 등록된 사람일 때
                article.friends_ids.get(id=request.user.id)
                return Response({'message':'이미 밥친구로 등록되어 있습니다.'}, status=status.HTTP_409_CONFLICT)
            except ObjectDoesNotExist:
                # 작성자 이외의 사람의 요청이고 새로 등록 되었을 때
                article.friends_ids.add(request.user)
                return Response({'message':'밥친구로 등록되었습니다.'}, status=status.HTTP_200_OK)

    def delete(self, request, article_id):
        """ 게시물 삭제 """
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.author_id:
            article.delete()
            return Response({'message':'삭제 되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        else:
          return Response({'message':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
