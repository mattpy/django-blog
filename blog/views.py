from datetime import date

from django.shortcuts import render

posts = [
    {
        "slug": "swimming-in-the-sea",
        "image": "dolphins.jpg",
        "author": "Matt",
        "date": date(2021, 8, 18),
        "title": "Dolphin Diving",
        "excerpt": "There's nothing like swimming with one of the world's smartest creatures to make you feel alive",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!
        """
    },
    {
        "slug": "the-best-ideas",
        "image": "idea.jpg",
        "author": "Matt",
        "date": date(2021, 8, 15),
        "title": "Idea Iteration",
        "excerpt": "Think smarter, not harder. Just keep swimming. Finding Nemo is one of the best Pixar movies",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!
        """
    },
    {
        "slug": "road-tripping",
        "image": "road-trip.jpg",
        "author": "Matt",
        "date": date(2021, 8, 10),
        "title": "Country Roads",
        "excerpt": "Take me home. John Denver is one the classic country artists. He liked guitars.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, id! Magni,
            ullam perspiciatis eligendi placeat quos iste labore libero, est sunt beatae
            et, repudiandae maiores. Ab, perferendis? Rerum, mollitia aperiam!
        """
    }
]


def starting_page(request):
    sorted_posts = sorted(posts, key=lambda post: post['date'])
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts_page(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': posts
    })


def post_detail(request, slug):
    selected_post = next(post for post in posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        'post': selected_post
    })
