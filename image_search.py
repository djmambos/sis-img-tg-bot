from distutils.log import error
import config
import random
from google_images_search import GoogleImagesSearch

IMG_COUNT_TO_SEARCH = 5

def search_img_by_name(img_name):
    gis = GoogleImagesSearch(config.GOOGLE_API_KEY, config.GOOGLE_CX)

    _search_params = {
        'q': img_name,
        'num': IMG_COUNT_TO_SEARCH,
        'safe': 'off',
        'fileType': 'jpg|gif|png',
        'rights': 'cc_noncommercial',
        'imgSize': 'huge',
    }

    try:
        gis.search(search_params=_search_params)
    except BaseException as error:
        print(error)

    return get_random_img_url_by_list(gis.results())

def get_random_img_url_by_list(search_result):
    img_urls = []

    for image in search_result:
        img_urls.append(image.url)

    if img_urls:
        return random.choice(img_urls)

    return img_urls