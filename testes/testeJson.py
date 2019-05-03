posts = [
    {
        "images": {
            "low_res": {
                "url":"lowResUrl1",
                "width":0,
                "height":0
            },
            "thumb": {
                "url":"thumbUrl1",
                "width":0,
                "height":0
            },
            "default": {
                "url":"defaultUrl1",
                "width":0,
                "height":0
            }
        }
    },
    {
        "images": {
            "low_res": {
                "url":"lowResUrl2",
                "width":0,
                "height":0
            },
            "thumb": {
                "url":"thumbUrl2",
                "width":0,
                "height":0
            },
            "default": {
                "url":"defaultUrl2",
                "width":0,
                "height":0
            }
        }
    }
]

urls = list()
posts_data = [post['images'] for post in posts]
for post in posts_data:
    post_images_urls = [post['low_res']['url'], post['thumb']['url'], post['default']['url']]
    urls.append(post_images_urls)
print(urls)


# urls = [url for url in [item[1]["url"] for item in [post['images'].items() for post in posts]]]
# print(urls)