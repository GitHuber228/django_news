from django.db.models import Max

from comments.models import PostCommentModel


def get_comment_list_count_by_post_pk(pk: int):
    return PostCommentModel.objects.filter(post_id=pk).aggregate(Max('local_id'))


def get_parent_post_comment_by_pk(pk: int):
    return PostCommentModel.objects.get(pk=pk)
