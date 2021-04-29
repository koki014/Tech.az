import uuid
from django.db import models

# Create your models here.


class Comment(models.Model):
    # informations
    content = models.TextField("Komment", blank=False, null=False)
    comment_uuid = models.UUIDField('Comment ID', default=uuid.uuid1())

    # relation's
    owner = models.ForeignKey("account.User", on_delete=models.CASCADE)
    articles = models.ForeignKey("articles.Articles", related_name='articles_comments', on_delete=models.CASCADE, blank=True, null=True)
    videos = models.ForeignKey("videos.Video", related_name='videos_comments', on_delete=models.CASCADE, blank=True, null=True)
    news = models.ForeignKey("news.News", related_name='news_comments', on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        if self.articles:
            
            return "Comment by: {0} on {1}".format(self.owner.username, self.articles)
        if self.videos:
            return "Comment by: {0} on {1}".format(self.owner.username, self.videos)
        if self.news:
            return "Comment by: {0} on {1}".format(self.owner.username, self.news)
        return self.content
    
    def get_category(self):
        if self.articles:
            # print(self.articles.objects.get('title'))
            return "{0}".format(self.articles.id)
        if self.videos:
            return "{0}".format(self.videos.id)
        if self.news:
            return "{0}".format(self.news.id)
        return None

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return True
        return False

