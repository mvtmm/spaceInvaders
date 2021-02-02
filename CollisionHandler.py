import pygame
from Scenes import EndScreen


class CollisionHandler():
    def __init__(self, game):
        self.game = game

    def update(self):
        # Item einsammeln Kollision
        # Iteration über alle gespawnten Items
        for items in self.game.object.getObjects():
            # Check ob Spielership Items kollidieren
            if self.game.player.playerShip.playerShipRect.colliderect(items.itemRect):
                # Eigenschaft des Item verteilen
                items.trigger()

        # Iteration über alle Schüsse
        for projectile in self.game.player.getProjectileObjects():

            # Check ob Projectile Gegner treffen
            for enemy in self.game.enemys.getObjects():
                # Wenn Kollision besteht dann entfernen
                if enemy.shipRect.colliderect(projectile.projectile_Rect):
                    enemy.trigger()
                    # Projektil entfernen
                    self.game.player.RemovePlayerShoot(projectile)

            # Check ob Meteore getroffen wurden
            for items in self.game.object.getObjects():
               # Wenn Meteor und Kollision besteht dann entfernen
                if type(items).__name__ == "MeteorItemObject" and items.itemRect.colliderect(projectile.projectile_Rect):
                    items.projectileTrigger()
                    self.game.player.RemovePlayerShoot(projectile)

        # Gegnerische Schüsse Kollision hinterlegen
        for enemyprojectile in self.game.enemys.getProjectileObjects():
            if enemyprojectile.projectile_Rect is not None:
                if self.game.player.playerShip.playerShipRect.colliderect(enemyprojectile.projectile_Rect):
                    self.game.player.decreaseHealth(25)
                    self.game.enemys.RemoveEnemyShoot(enemyprojectile)

        # Überprüfung ob Enemys untere Border treffen dann losescreen
        border = pygame.Rect(0, 700, 1200, 1000)
        for enemy in self.game.enemys.getObjects():
            if enemy.shipRect.colliderect(border):
                self.game.quitgame = True
                self.game.next.SwitchToScene(EndScreen.EndScreen())
