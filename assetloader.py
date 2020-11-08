import pygame
import os
from assettype import AssetType


class Assetloader:

    def getAsset(_assettype: AssetType, filename):
          
        _gamefolder             = os.path.dirname(__file__)
        _assetsfolder           = os.path.join(_gamefolder, 'data')
        _graphicsfolder         = os.path.join(_assetsfolder, 'img')
        _soundfolder            = os.path.join(_assetsfolder, 'sound')
        _objectfolder           = os.path.join(_graphicsfolder, 'objects')

        if _assettype == AssetType.Graphics:
            _data = pygame.image.load(os.path.join(_graphicsfolder, filename))
            return _data
        elif _assettype == AssetType.Sound:
            _data = pygame.image.load(os.path.join(_soundfolder, filename))
            return _data
        elif _assettype == AssetType.Items:
            _data = pygame.image.load(os.path.join(_objectfolder, filename))
            return _data
   
           



