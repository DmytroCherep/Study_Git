import requests

BASE_URL = "https://images-api.nasa.gov"


def get_nasa_ids():
    search_url = f"{BASE_URL}/search"
    params = {
        "q": "Curiosity rover Mars",
        "media_type": "image",
        "page_size": 20
    }

    response = requests.get(search_url, params=params)
    data = response.json()

    items = data["collection"]["items"]

    nasa_ids = []
    for item in items:
        nasa_id = item["data"][0]["nasa_id"]
        nasa_ids.append(nasa_id)

    return nasa_ids


def get_image_url(nasa_id):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"

    response = requests.get(asset_url)
    data = response.json()

    items = data["collection"]["items"]

    for item in items:
        href = item["href"]
        if href.endswith(".jpg"):
            return href

    return None


def download_image(url, filename):
    response = requests.get(url)

    with open(filename, "wb") as f:
        f.write(response.content)


def main():
    nasa_ids = get_nasa_ids()

    images_downloaded = 0

    for nasa_id in nasa_ids:
        image_url = get_image_url(nasa_id)

        if image_url:
            filename = f"mars_photo{images_downloaded + 1}.jpg"
            download_image(image_url, filename)

            print(f"Downloaded: {filename}")

            images_downloaded += 1

        if images_downloaded == 2:
            break


if __name__ == "__main__":
    main()