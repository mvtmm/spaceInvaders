import pygame
import os
from assettype import AssetType


class Assetloader:

    def getAsset(AssetType, filename):

        _gamefolder             = os.path.dirname(__file__)
        _assetsfolder           = os.path.join(_gamefolder, 'data')
        _graphicsfolder         = os.path.join(_assetsfolder, 'img')
        _soundfolder            = os.path.join(_assetsfolder, 'sound')

        if (AssetType.Graphics):
            _img = pygame.image.load(os.path.join(_graphicsfolder, filename))
            return _img


