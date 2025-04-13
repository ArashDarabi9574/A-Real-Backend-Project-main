from django.core.management.base import BaseCommand
from faker import Faker
from shop.models import Product, Brand
from blog.models import Post, PostCategory, PostComment
import random
from datetime import datetime
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    help = 'Insert shop dummy data'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker(['fa-ir',])
        self.fake2 = Faker(['en-US'])

    def handle(self, *args, **options):
        user = User.objects.create_user(
            phone_number=self.fake.phone_number(), password='asdfg12345', first_name=self.fake.name(), email=self.fake2.email(),
        )

        user_list = User.objects.all()
        for _ in range(5):
            Brand.objects.create(
                title=self.fake2.text(max_nb_chars=15),
                description=self.fake.paragraph(nb_sentences=35),
                country=self.fake.country(),
                thumbnail=self.fake.image_url(),
            )
            brand_list = Brand.objects.all()

            # PostCategory.objects.create(
            #     title=self.fake.text(max_nb_chars=10),
            # )
            # category_list = PostCategory.objects.all()

            # Post.objects.create(
            #     category=PostCategory.objects.get(
            #         title=random.choice(category_list)),
            #     title=self.fake.text(max_nb_chars=15),
            #     author=user,
            #     status=random.choice(['publish', 'archive', 'pending']),
            #     content=self.fake.paragraph(nb_sentences=35),
            #     short_description=self.fake.paragraph(nb_sentences=10),
            #     thumbnail=self.fake.image_url(),
            #     )
            # post_list = Post.objects.all()
            # PostComment(
            #     post = Post.objects.get(title=random.choice(post_list)),
            #     user = User.objects.get(phone_number=random.choice(user_list)),
            #     message=self.fake.paragraph(nb_sentences=10),
            # )
            # Product.objects.create(
            #     created_at=datetime.now(),
            #     status=random.choice(['pre_order', 'out_stock', 'in_stock']),
            #     title=self.fake.text(max_nb_chars=15),
            #     content=self.fake.paragraph(nb_sentences=35),
            #     main_price=self.fake2.pyint(
            #         min_value=1200000, max_value=10000000),
            #     inventory=self.fake2.pyint(min_value=0, max_value=10),
            #     author=user,
            #     extra_price=self.fake2.pyint(
            #         min_value=0, max_value=20000),
            #     price_deadline=random.choice([True, False]),
            #     thumbnail=self.fake.image_url(),
            # )

            # Branch.objects.create(
            #     title=self.fake.text(max_nb_chars=10),
            #     description=self.fake.paragraph(nb_sentences=25),
            #     inventory=self.fake2.random_digit_not_null(),
            #     extra_price=self.fake2.pyint(min_value=1200000, max_value=10000000),
            #
            # )
