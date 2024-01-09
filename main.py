@namespace
class SpriteKind:
    Big_sprite = SpriteKind.create()
    points = SpriteKind.create()

def on_left_pressed():
    if Players.kind() == SpriteKind.Big_sprite:
        animation.run_image_animation(Players,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 7 7 7 7 7 7 7 f . . . 
                                . . . f f 7 7 7 7 7 7 7 7 f . . 
                                . . . . . f 7 7 7 f 7 7 7 7 f . 
                                . . . . . . f 7 7 7 7 7 7 7 f . 
                                . . . . . . . f 7 7 7 7 7 7 f . 
                                . . . . . . . . f 7 7 7 7 7 f . 
                                . . . . . . . f 7 7 7 7 7 7 f . 
                                . . . . . . f 7 7 7 7 7 7 7 f . 
                                . . . . . f 7 7 7 7 7 7 7 7 f . 
                                . . . f f 7 7 7 7 7 7 7 7 f . . 
                                . . . . f 7 7 7 7 7 7 7 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 7 7 7 7 7 7 7 f . . . 
                                . . . f f 7 7 7 7 7 7 7 7 f . . 
                                . . f 7 7 7 7 f 7 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . f f f f f f f 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . . f f 7 7 7 7 7 7 7 7 f . . 
                                . . . . f 7 7 7 7 7 7 7 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 7 7 7 7 7 7 7 f . . . 
                                . . . f f 7 7 7 7 7 7 7 7 f . . 
                                . . . . . f 7 7 7 f 7 7 7 7 f . 
                                . . . . . . f 7 7 7 7 7 7 7 f . 
                                . . . . . . . f 7 7 7 7 7 7 f . 
                                . . . . . . . . f 7 7 7 7 7 f . 
                                . . . . . . . f 7 7 7 7 7 7 f . 
                                . . . . . . f 7 7 7 7 7 7 7 f . 
                                . . . . . f 7 7 7 7 7 7 7 7 f . 
                                . . . f f 7 7 7 7 7 7 7 7 f . . 
                                . . . . f 7 7 7 7 7 7 7 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 7 7 7 7 7 7 7 f . . . 
                                . . . f f 7 7 7 7 7 7 7 7 f . . 
                                . . f 7 7 7 7 f 7 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . f f f f f f f 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . f 7 7 7 7 7 7 7 7 7 7 7 f . 
                                . . . f f 7 7 7 7 7 7 7 7 f . . 
                                . . . . f 7 7 7 7 7 7 7 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            100,
            True)
    else:
        animation.run_image_animation(Players,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . f f 5 5 5 5 5 5 5 5 f . . 
                                . . . . . f 5 5 5 f 5 5 5 5 f . 
                                . . . . . . f 5 5 5 5 5 5 5 f . 
                                . . . . . . . f 5 5 5 5 5 5 f . 
                                . . . . . . . . f 5 5 5 5 5 f . 
                                . . . . . . . f 5 5 5 5 5 5 f . 
                                . . . . . . f 5 5 5 5 5 5 5 f . 
                                . . . . . f 5 5 5 5 5 5 5 5 f . 
                                . . . f f 5 5 5 5 5 5 5 5 f . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . f f 5 5 5 5 5 5 5 5 f . . 
                                . . f 5 5 5 5 f 5 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f f f f f f f 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . . f f 5 5 5 5 5 5 5 5 f . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . f f 5 5 5 5 5 5 5 5 f . . 
                                . . . . . f 5 5 5 f 5 5 5 5 f . 
                                . . . . . . f 5 5 5 5 5 5 5 f . 
                                . . . . . . . f 5 5 5 5 5 5 f . 
                                . . . . . . . . f 5 5 5 5 5 f . 
                                . . . . . . . f 5 5 5 5 5 5 f . 
                                . . . . . . f 5 5 5 5 5 5 5 f . 
                                . . . . . f 5 5 5 5 5 5 5 5 f . 
                                . . . f f 5 5 5 5 5 5 5 5 f . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . f f 5 5 5 5 5 5 5 5 f . . 
                                . . f 5 5 5 5 f 5 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f f f f f f f 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . . f f 5 5 5 5 5 5 5 5 f . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            100,
            True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap(sprite, otherSprite):
    global pointsnum
    sprites.destroy(otherSprite)
    info.change_score_by(1)
    pointsnum += -1
sprites.on_overlap(SpriteKind.player, SpriteKind.points, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_score_by(list2._pick_random())
    sprites.destroy(otherSprite2)
sprites.on_overlap(SpriteKind.Big_sprite, SpriteKind.enemy, on_on_overlap2)

def on_right_pressed():
    if Players.kind() == SpriteKind.Big_sprite:
        animation.run_image_animation(Players,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 7 7 7 7 7 7 7 f . . . . 
                                . . f 7 7 7 7 7 7 7 7 f f . . . 
                                . f 7 7 7 7 f 7 7 7 f . . . . . 
                                . f 7 7 7 7 7 7 7 f . . . . . . 
                                . f 7 7 7 7 7 7 f . . . . . . . 
                                . f 7 7 7 7 7 f . . . . . . . . 
                                . f 7 7 7 7 7 7 f . . . . . . . 
                                . f 7 7 7 7 7 7 7 f . . . . . . 
                                . f 7 7 7 7 7 7 7 7 f . . . . . 
                                . . f 7 7 7 7 7 7 7 7 f f . . . 
                                . . . f 7 7 7 7 7 7 7 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 7 7 7 7 7 7 7 f . . . . 
                                . . f 7 7 7 7 7 7 7 7 f f . . . 
                                . f 7 7 7 7 7 7 f 7 7 7 7 f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . f 7 7 7 7 7 f f f f f f f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . . f 7 7 7 7 7 7 7 7 f f . . . 
                                . . . f 7 7 7 7 7 7 7 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 7 7 7 7 7 7 7 f . . . . 
                                . . f 7 7 7 7 7 7 7 7 f f . . . 
                                . f 7 7 7 7 f 7 7 7 f . . . . . 
                                . f 7 7 7 7 7 7 7 f . . . . . . 
                                . f 7 7 7 7 7 7 f . . . . . . . 
                                . f 7 7 7 7 7 f . . . . . . . . 
                                . f 7 7 7 7 7 7 f . . . . . . . 
                                . f 7 7 7 7 7 7 7 f . . . . . . 
                                . f 7 7 7 7 7 7 7 7 f . . . . . 
                                . . f 7 7 7 7 7 7 7 7 f f . . . 
                                . . . f 7 7 7 7 7 7 7 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 7 7 7 7 7 7 7 f . . . . 
                                . . f 7 7 7 7 7 7 7 7 f f . . . 
                                . f 7 7 7 7 7 7 f 7 7 7 7 f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . f 7 7 7 7 7 f f f f f f f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . f 7 7 7 7 7 7 7 7 7 7 7 f . . 
                                . . f 7 7 7 7 7 7 7 7 f f . . . 
                                . . . f 7 7 7 7 7 7 7 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            100,
            True)
    else:
        animation.run_image_animation(Players,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 f f . . . 
                                . f 5 5 5 5 f 5 5 5 f . . . . . 
                                . f 5 5 5 5 5 5 5 f . . . . . . 
                                . f 5 5 5 5 5 5 f . . . . . . . 
                                . f 5 5 5 5 5 f . . . . . . . . 
                                . f 5 5 5 5 5 5 f . . . . . . . 
                                . f 5 5 5 5 5 5 5 f . . . . . . 
                                . f 5 5 5 5 5 5 5 5 f . . . . . 
                                . . f 5 5 5 5 5 5 5 5 f f . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 f f . . . 
                                . f 5 5 5 5 5 5 f 5 5 5 5 f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 5 5 5 5 f f f f f f f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . . f 5 5 5 5 5 5 5 5 f f . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 f f . . . 
                                . f 5 5 5 5 f 5 5 5 f . . . . . 
                                . f 5 5 5 5 5 5 5 f . . . . . . 
                                . f 5 5 5 5 5 5 f . . . . . . . 
                                . f 5 5 5 5 5 f . . . . . . . . 
                                . f 5 5 5 5 5 5 f . . . . . . . 
                                . f 5 5 5 5 5 5 5 f . . . . . . 
                                . f 5 5 5 5 5 5 5 5 f . . . . . 
                                . . f 5 5 5 5 5 5 5 5 f f . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 f f . . . 
                                . f 5 5 5 5 5 5 f 5 5 5 5 f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 5 5 5 5 f f f f f f f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . . f 5 5 5 5 5 5 5 5 f f . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            100,
            True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap3(sprite3, otherSprite3):
    sprites.destroy(otherSprite3)
    Players.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . f f f f f f f . . . . . 
                . . . f 7 7 7 7 7 7 7 f . . . . 
                . . f 7 7 7 7 7 7 7 7 f f . . . 
                . f 7 7 7 7 f 7 7 7 f . . . . . 
                . f 7 7 7 7 7 7 7 f . . . . . . 
                . f 7 7 7 7 7 7 f . . . . . . . 
                . f 7 7 7 7 7 f . . . . . . . . 
                . f 7 7 7 7 7 7 f . . . . . . . 
                . f 7 7 7 7 7 7 7 f . . . . . . 
                . f 7 7 7 7 7 7 7 7 f . . . . . 
                . . f 7 7 7 7 7 7 7 7 f f . . . 
                . . . f 7 7 7 7 7 7 7 f . . . . 
                . . . . f f f f f f f . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    Players.set_kind(SpriteKind.Big_sprite)
    info.change_score_by(list2._pick_random())
    pause(10000)
    Players.set_kind(SpriteKind.player)
    Players.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . f f f f f f f . . . . . 
                . . . f 5 5 5 5 5 5 5 f . . . . 
                . . f 5 5 5 5 5 5 5 5 f f . . . 
                . f 5 5 5 5 f 5 5 5 f . . . . . 
                . f 5 5 5 5 5 5 5 f . . . . . . 
                . f 5 5 5 5 5 5 f . . . . . . . 
                . f 5 5 5 5 5 f . . . . . . . . 
                . f 5 5 5 5 5 5 f . . . . . . . 
                . f 5 5 5 5 5 5 5 f . . . . . . 
                . f 5 5 5 5 5 5 5 5 f . . . . . 
                . . f 5 5 5 5 5 5 5 5 f f . . . 
                . . . f 5 5 5 5 5 5 5 f . . . . 
                . . . . f f f f f f f . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    global pointsnum
    sprites.destroy(otherSprite4)
    info.change_score_by(1)
    pointsnum += -1
sprites.on_overlap(SpriteKind.Big_sprite, SpriteKind.points, on_on_overlap4)

def on_on_overlap5(sprite5, otherSprite5):
    game.splash("Game Over")
    game.splash("Score:" + str(info.score()))
    game.reset()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap5)

powerup: Sprite = None
points2: Sprite = None
Players: Sprite = None
list2: List[number] = []
info.set_score(0)
pointsnum = 200
list2 = [5, 10, 50, 100]
powerups = game.ask_for_number("Difficulty (1-3)", 1)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
Players = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . f f f f f f f . . . . . 
            . . . f 5 5 5 5 5 5 5 f . . . . 
            . . f 5 5 5 5 5 5 5 5 f f . . . 
            . f 5 5 5 5 f 5 5 5 f . . . . . 
            . f 5 5 5 5 5 5 5 f . . . . . . 
            . f 5 5 5 5 5 5 f . . . . . . . 
            . f 5 5 5 5 5 f . . . . . . . . 
            . f 5 5 5 5 5 5 f . . . . . . . 
            . f 5 5 5 5 5 5 5 f . . . . . . 
            . f 5 5 5 5 5 5 5 5 f . . . . . 
            . . f 5 5 5 5 5 5 5 5 f f . . . 
            . . . f 5 5 5 5 5 5 5 f . . . . 
            . . . . f f f f f f f . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
tiles.place_on_tile(Players, tiles.get_tile_location(16, 18))
ghostp = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f f . . . . 
            . . . . f 3 3 3 3 3 3 3 f . . . 
            . . . . f 3 1 1 3 1 1 3 f . . . 
            . . . . f 3 1 6 3 1 6 3 f . . . 
            . . . . f 3 3 3 3 3 3 3 f . . . 
            . . . . f 3 3 3 3 3 3 3 f . . . 
            . . . . f 3 3 3 3 3 3 3 f . . . 
            . . . . f 3 3 3 3 3 3 3 f . . . 
            . . . . f 3 3 3 3 3 3 3 f . . . 
            . . . . f 3 3 3 3 3 3 3 f . . . 
            . . . . f 3 3 3 3 3 3 3 f . . . 
            . . . . f 3 f 3 f 3 f 3 f . . . 
            . . . . . f . f . f . f . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
tiles.place_on_tile(ghostp, tiles.get_tile_location(3, 30))
ghostb = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f f . . . . 
            . . . . f 9 9 9 9 9 9 9 f . . . 
            . . . . f 9 1 1 9 1 1 9 f . . . 
            . . . . f 9 1 6 9 1 6 9 f . . . 
            . . . . f 9 9 9 9 9 9 9 f . . . 
            . . . . f 9 9 9 9 9 9 9 f . . . 
            . . . . f 9 9 9 9 9 9 9 f . . . 
            . . . . f 9 9 9 9 9 9 9 f . . . 
            . . . . f 9 9 9 9 9 9 9 f . . . 
            . . . . f 9 9 9 9 9 9 9 f . . . 
            . . . . f 9 9 9 9 9 9 9 f . . . 
            . . . . f 9 f 9 f 9 f 9 f . . . 
            . . . . . f . f . f . f . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
tiles.place_on_tile(ghostb, tiles.get_tile_location(29, 29))
ghostr = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f f . . . . 
            . . . . f 2 2 2 2 2 2 2 f . . . 
            . . . . f 2 1 1 2 1 1 2 f . . . 
            . . . . f 2 1 6 2 1 6 2 f . . . 
            . . . . f 2 2 2 2 2 2 2 f . . . 
            . . . . f 2 2 2 2 2 2 2 f . . . 
            . . . . f 2 2 2 2 2 2 2 f . . . 
            . . . . f 2 2 2 2 2 2 2 f . . . 
            . . . . f 2 2 2 2 2 2 2 f . . . 
            . . . . f 2 2 2 2 2 2 2 f . . . 
            . . . . f 2 2 2 2 2 2 2 f . . . 
            . . . . f 2 f 2 f 2 f 2 f . . . 
            . . . . . f . f . f . f . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
tiles.place_on_tile(ghostr, tiles.get_tile_location(30, 1))
ghosto = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f f . . . . 
            . . . . f 4 4 4 4 4 4 4 f . . . 
            . . . . f 4 1 1 4 1 1 4 f . . . 
            . . . . f 4 1 6 4 1 6 4 f . . . 
            . . . . f 4 4 4 4 4 4 4 f . . . 
            . . . . f 4 4 4 4 4 4 4 f . . . 
            . . . . f 4 4 4 4 4 4 4 f . . . 
            . . . . f 4 4 4 4 4 4 4 f . . . 
            . . . . f 4 4 4 4 4 4 4 f . . . 
            . . . . f 4 4 4 4 4 4 4 f . . . 
            . . . . f 4 4 4 4 4 4 4 f . . . 
            . . . . f 4 f 4 f 4 f 4 f . . . 
            . . . . . f . f . f . f . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
tiles.place_on_tile(ghosto, tiles.get_tile_location(1, 1))
ghostb.follow(Players, 40)
ghosto.follow(Players, 40)
ghostp.follow(Players, 40)
ghostr.follow(Players, 40)
for index in range(200):
    points2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . 4 5 5 4 . . . . . . 
                    . . . . . . 2 5 5 2 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.points)
    tiles.place_on_random_tile(points2, assets.tile("""
        transparency16
    """))
if powerups == 0:
    game.reset()
elif powerups == 1:
    powerup = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . 4 5 5 5 5 4 . . . . . 
                    . . . . . 4 5 5 5 5 4 . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    tiles.place_on_random_tile(powerup, assets.tile("""
        transparency16
    """))
    powerup.set_kind(SpriteKind.food)
    controller.move_sprite(Players)
    Players.set_velocity(10, 10)
elif powerups == 2:
    for index2 in range(2):
        powerup = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 4 4 . . . . . . . 
                            . . . . . . 5 5 5 5 . . . . . . 
                            . . . . . 4 5 5 5 5 4 . . . . . 
                            . . . . . 4 5 5 5 5 4 . . . . . 
                            . . . . . . 5 5 5 5 . . . . . . 
                            . . . . . . . 4 4 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_random_tile(powerup, assets.tile("""
            transparency16
        """))
        powerup.set_kind(SpriteKind.food)
    controller.move_sprite(Players)
    Players.set_velocity(10, 10)
elif powerups == 3:
    for index3 in range(3):
        powerup = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 4 4 . . . . . . . 
                            . . . . . . 5 5 5 5 . . . . . . 
                            . . . . . 4 5 5 5 5 4 . . . . . 
                            . . . . . 4 5 5 5 5 4 . . . . . 
                            . . . . . . 5 5 5 5 . . . . . . 
                            . . . . . . . 4 4 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_random_tile(powerup, assets.tile("""
            transparency16
        """))
        powerup.set_kind(SpriteKind.food)
    controller.move_sprite(Players)
    Players.set_velocity(10, 10)
else:
    game.reset()
if pointsnum == 0:
    game.splash("YOU WIN")
    game.splash("Score" + str(info.score()))
    game.reset()

def on_forever():
    scene.camera_follow_sprite(Players)
forever(on_forever)
