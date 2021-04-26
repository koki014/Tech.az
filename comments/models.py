from django.db import models

# Create your models here.


class Comment(models.Model):
    # informations
    content = models.TextField("Komment", blank=False, null=False)

    # relation's
    articles = models.ForeignKey("articles.Articles", related_name='articles_comments', on_delete=models.CASCADE, blank=True, null=True)
    videos = models.ForeignKey("videos.Video", related_name='videos_comments', on_delete=models.CASCADE, blank=True, null=True)
    news = models.ForeignKey("news.News", related_name='news_comments', on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey("account.User", on_delete=models.CASCADE)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.articles:
            return self.articles
        if self.videos:
            return self.videos
        if self.news:
            return self.news
        return self.content

