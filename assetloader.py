import pygame
import os
from assettype import AssetType


# Klasse zum Laden von Objekten
class Assetloader:
    # Methode um Objekte zu laden
    def getAsset(_assettype: AssetType, filename):
        # Pfade zusammenbasteln
        _gamefolder             = os.path.dirname(__file__)
        # Spielordner data Ordner
        _assetsfolder           = os.path.join(_gamefolder, 'data')
        # Spielordner / data / img Ordner 
        _graphicsfolder         = os.path.join(_assetsfolder, 'img')
        # Spielordner / data / sound Ordner 
        _soundfolder            = os.path.join(_assetsfolder, 'sound')
        # Spielordner / data / objects Ordner 
        _objectfolder           = os.path.join(_graphicsfolder, 'objects')

        # Überprüfen ob das zu ladene Objekt eine Grafik ist
        if _assettype == AssetType.Graphics:
            _data = pygame.image.load(os.path.join(_graphicsfolder, filename))
            return _data

        # Überprüfen ob das zu ladene Objekt Musik ist
        elif _assettype == AssetType.Sound:
            _data = pygame.image.load(os.path.join(_soundfolder, filename))
            return _data

        # Überprüfen ob das zu ladene Objekt Item ist
        elif _assettype == AssetType.Items:
            _data = pygame.image.load(os.path.join(_objectfolder, filename))
            return _data
   
           



