python manage.py shell
from django.db import models
from django.contrib.auth.models import User
from param import *
from django.db.models import Sum
from news.models import *
	dir()

	u1 = User.objects.create(username='User1')
	u2 = User.objects.create(username='User2')

	Author.objects.create(authorUser=u1)
	Author.objects.create(authorUser=u2)
	
    Category.objects.create(name='Politics')
	Category.objects.create(name='Economy')
	Category.objects.create(name='Incidents')
	Category.objects.create(name='Culture')

	au1 = Author.objects.get(id=1)
	au2 = Author.objects.get(id=2)
	Post.objects.create(author=au1  , categoryType= 'AR', title='The article of the first author ', text='here is the first text of the first author about incidents and politics')
	Post.objects.create(author=au2  , categoryType= 'AR', title='The article of the second author ', text='here is the first text of the second author about culture')
	Post.objects.create(author=au2  , categoryType= 'NW', title='The news of the second author ', text='here is the first news of the second author about culture')

	Post.objects.get(id=2).preview() 

	Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1)) 
	Post.objects.get(id=1).postCategory.add(Category.objects.get(id=3))
	Post.objects.get(id=2).postCategory.add(Category.objects.get(id=4))

	Comment.objects.create(commentPost=Post.objects.get(id=1), userPost=Author.objects.get(id=1).authorUser, text='comment on the policy in the first article from author 1')
	Comment.objects.create(commentPost=Post.objects.get(id=1), userPost=Author.objects.get(id=2).authorUser, text='comment on the policy in the first article from author 2')
	Comment.objects.create(commentPost=Post.objects.get(id=2), userPost=Author.objects.get(id=1).authorUser, text='comment on the Culture in the second article from author 1')
	Comment.objects.create(commentPost=Post.objects.get(id=2), userPost=Author.objects.get(id=2).authorUser, text='comment on the Culture in the second article from author 2')

    Post.objects.get(id=1).like()
	Post.objects.get(id=1).dislike()
	Post.objects.get(id=2).like()
	Post.objects.get(id=2).dislike()

	Comment.objects.get(id=1).like()
	Comment.objects.get(id=1).dislike()
	Comment.objects.get(id=2).like()
	Comment.objects.get(id=2).dislike()

	Comment.objects.get(id=3).like()
	Comment.objects.get(id=3).dislike()

	Comment.objects.get(id=2).rating

    a1 = Author.objects.get(id=1)
	a1.update_rating()

	a1.ratingAuthor
	a1.post_set.all().values('rating')
	a1.authorUser.comment_set.all().values('rating')


	a2 = Author.objects.all().order_by('-ratingAuthor')[:1] 
	a2
	for b in a2:
		b.authorUser.username
		b.ratingAuthor

a3 = Post.objects.all().order_by('-rating')[:1]
for j in a3:
	f"Data : {j.dataCreations.day}"
	f"Rating: {j.rating}"
	j.author.authorUser
	j.title
	j.preview()

a4 = Comment.objects.all().filter(commentPost=a3)

for d in a4:
	F"Data : {d.dataCreation.day}/{d.dataCreation.month}/{d.dataCreation.year}"
	d.userPost
	F"Rating : {d.rating}"
	d.text