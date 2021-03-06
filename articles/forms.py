from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', ]
        # fields = ['title', ]


class CommentForm(forms.ModelForm):
    # aritcle = forms.ModelChoiceField(
    #     queryset=Article.objects.all(),
    # )

    content = forms.CharField(
        label='댓글',
    )

    class Meta:
        model = Comment
        fields = ['content',]
