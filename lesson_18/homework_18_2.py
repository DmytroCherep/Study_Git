import requests

BASE_URL = "http://127.0.0.1:8080"


def upload_image(file_path):
    url = f"{BASE_URL}/upload"

    with open(file_path, "rb") as f:
        files = {"image": f}
        response = requests.post(url, files=files)

    data = response.json()
    print("Uploaded:", data)

    return data["image_url"]


def get_image(filename):
    url = f"{BASE_URL}/image/{filename}"

    response = requests.get(url, headers={"Content-Type": "text"})
    print("GET response:", response.json())


def delete_image(filename):
    url = f"{BASE_URL}/delete/{filename}"

    response = requests.delete(url)
    print("DELETE response:", response.json())


def main():
    # ВАЖЛИВО: файл має існувати!
    file_path = "test.jpg"

    # 1️⃣ upload
    image_url = upload_image(file_path)

    # витягуємо ім’я файлу
    filename = image_url.split("/")[-1]

    # 2️⃣ get
    get_image(filename)

    # 3️⃣ delete
    delete_image(filename)


if __name__ == "__main__":
    main()