import os
import json
import random
from image_processing import get_random_image, get_average_color, find_nearest_color, upload_image_to_imgur
from text_processing import get_random_text
from blogger_api import authenticate_blogger_api, create_blogger_post

wallpapers_folder = './wallpapers'  # Set the correct path to wallpapers
posts_folder = './posts'  # Set the correct path to text posts

IMGUR_CLIENT_ID = 'xxxxxxxxxxxxxxx'  # Use your Imgur Client ID here

def get_random_title(json_file):
    with open(json_file, 'r') as f:
        titles_data = json.load(f)
        return random.choice(titles_data['titles'])

def main():
    image_path = get_random_image(wallpapers_folder)

    post_content = get_random_text(posts_folder)

    avg_color = get_average_color(image_path)

    nearest_color = find_nearest_color(avg_color)

    image_url = upload_image_to_imgur(image_path, IMGUR_CLIENT_ID)

    random_title = get_random_title('titles.json')  # Path to your titles JSON file
    post_title = f"{random_title} - {nearest_color.capitalize()} Vibes"

    service = authenticate_blogger_api()

    blog_id = 'YOUR_BLOG_ID'  # Replace with your actual Blogger Blog ID
    labels = [nearest_color]
    post = create_blogger_post(service, blog_id, post_title, post_content, image_url, labels, alt_text=post_title, img_title=post_title)
    print(f"Post created: {post['url']}")
    try:
        os.remove(image_path)
        print(f"Deleted local image: {image_path}")
    except Exception as e:
        print(f"Error deleting image: {e}")

if __name__ == "__main__":
    main()
