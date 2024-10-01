# Blogger Image Post Automation

## Description

This project automates the process of creating blog posts on Blogger by combining random wallpapers and text. It uploads an image to Imgur, retrieves a random text from a specified directory, calculates the image's average color, and creates a blog post with an image, title, and download link. The blog post is styled using Arial font for better readability.

### Features

- Selects a random image from a local wallpapers directory.
- Picks a random text file from a local posts directory.
- Calculates the average color of the selected image.
- Uploads the image to Imgur and retrieves its URL.
- Creates a blog post on Blogger with the image and text content.
- Includes a download button for the uploaded image.
- Applies Arial font styling to the blog post content.
- Deletes the local image after successful upload to prevent reuse.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.6 or higher
- Required Python libraries:
  - `Pillow`
  - `Matplotlib`
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `google-api-python-client`
  - `oauth2client`

You can install the required libraries using pip:

```bash
pip install Pillow matplotlib google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client oauth2client
```

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mrxehmad/blogger-image-post-automation.git
   cd blogger-image-post-automation
   ```

2. **Create the Necessary Folders**

   Ensure you have the following folder structure:

   ```
   blogger-image-post-automation/
   ├── wallpapers/     # Place your wallpaper images here
   ├── posts/         # Place your text files here
   ├── titles.json    # JSON file containing titles for blog posts
   ├── main.py        # Main script for posting to Blogger
   ├── blogger_api.py # API functions for Blogger
   ├── image_processing.py # Functions for processing images
   └── text_processing.py   # Functions for processing text
   ```

3. **Configure Your API Credentials**

   - **Blogger API**: Follow the [Blogger API documentation](https://developers.google.com/blogger/docs/3.0/using#OAuth2) to set up OAuth 2.0 and obtain your credentials (Client ID and Client Secret).
   - **Imgur API**: Sign up for an account on [Imgur](https://imgur.com/) and register an application to obtain your Imgur Client ID.

4. **Update Your Credentials in the Code**

   Replace the placeholders in the code with your actual Blogger and Imgur API credentials.

## Usage

Run the main script to create a new blog post:

```bash
python main.py
```

Upon successful execution, a new blog post will be created on your Blogger account, including a randomly selected image and corresponding text content.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, feel free to reach out to me at [ahmadfarazwarrich@gmail.com](mailto:ahmadfarazwarrich@gmail.com).
