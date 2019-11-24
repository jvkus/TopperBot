import argparse
import io
import base64

from oauth2client.client import GoogleCredentials
from googleapiclient import discovery, errors
from google.cloud import vision, storage
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

#Detects text from local file.#
def findtextlocal(path):
    with io.open(path,'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    #Prints extracted text.#
    for text in texts:
        print("\n'{}'".format(text.description))

#Text detection for online image. Only works with Google storage URIs.#
def findtextlink(uri):
    image = types.Image()
    image.source.image_uri = uri
    boop = client.text_detection(image=image)
    texts = boop.text_annotations

    for text in texts:
        print('\n"{}"'.format(text.description))

findtextlocal("G:\Storage\dev\TopperBot\TopperBot\TopperBot\sample3.png")