from app.models import *
from faker import Faker
from django.core.management.base import BaseCommand
from datetime import *
import random

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--ratio', dest='ratio',required=True)
    def handle(self,*args,**options):
        f = Faker()
        k = int(options['ratio'])
        users_to_add = []
        for i in range(k):
            l = f.user_name() + str(i)
            n = l + '123'
            e = f.email()
            p = f.password()
            user = CustomUser(password = p, email = e, login = l, nickname = n)
            users_to_add.append(user)
        created_Users = CustomUser.objects.bulk_create(users_to_add,batch_size=150)
        print(f'Было создано {len(created_Users)} пользователей')

        questions_to_add = []
        for i in range(k*10):
            CreateUser_id = random.randint(1,CustomUser.objects.count())
            q = Question(title="Текст-рыба" + str(i), text=f.paragraph(),created_at = datetime.now(),author_id = CreateUser_id )
            questions_to_add.append(q)
        created_q = Question.objects.bulk_create(questions_to_add,150)
        print(f'Было создано {len(created_q)} вопросов')
        answers_to_add = []
        kol = Question.objects.count()
        user_kol = CustomUser.objects.count()
        for i in range(k*100):
            a = Answer(user_id = random.randint(1,user_kol), question_id = random.randint(1,kol), text=f.paragraph())
            answers_to_add.append(a)
        created_a = Answer.objects.bulk_create(answers_to_add,150)
        print(f'Было создано {len(created_a)} ответов')
        tags_to_add = []
        for i in range(k):
            a = Tag(Name= f.word()+str(i))
            tags_to_add.append(a)
        created_t = Tag.objects.bulk_create(tags_to_add,150)
        print(f'Было создано {len(created_t)} тегов')

        likes_to_add = []
        for i in range(k*200):
            a = Like(question_id= random.randint(1,kol), author_id = random.randint(1,user_kol))
            likes_to_add.append(a)
        created_l = Like.objects.bulk_create(likes_to_add,150)
        print(f'Было создано {len(created_l)} лайков')

        # tagsKol = Tag.objects.count()
        # tags  = Tag.objects.all()
        # questions = Question.objects.all()
        # for i in questions:
        #     i.tags.clear()
        #     i.tags.add(tags[random.randint(1,tagsKol-1)])
        #     i.save()

