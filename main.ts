namespace SpriteKind {
    export const Big_sprite = SpriteKind.create()
    export const points = SpriteKind.create()
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Players.kind() == SpriteKind.Big_sprite) {
        animation.runImageAnimation(
        Players,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
    } else {
        animation.runImageAnimation(
        Players,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.points, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    info.changeScoreBy(1)
    pointsnum += -1
})
sprites.onOverlap(SpriteKind.Big_sprite, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeScoreBy(list._pickRandom())
    sprites.destroy(otherSprite)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Players.kind() == SpriteKind.Big_sprite) {
        animation.runImageAnimation(
        Players,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
    } else {
        animation.runImageAnimation(
        Players,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    Players.setImage(img`
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
        `)
    Players.setKind(SpriteKind.Big_sprite)
    info.changeScoreBy(list._pickRandom())
    pause(10000)
    Players.setKind(SpriteKind.Player)
    Players.setImage(img`
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
        `)
})
sprites.onOverlap(SpriteKind.Big_sprite, SpriteKind.points, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    info.changeScoreBy(1)
    pointsnum += -1
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    game.splash("Game Over")
    game.splash("Score:" + info.score())
    game.reset()
})
let powerup: Sprite = null
let points: Sprite = null
let Players: Sprite = null
let list: number[] = []
info.setScore(0)
let pointsnum = 200
list = [
5,
10,
50,
100
]
let powerups = game.askForNumber("Difficulty (1-3)", 1)
tiles.setCurrentTilemap(tilemap`level1`)
Players = sprites.create(img`
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
    `, SpriteKind.Player)
tiles.placeOnTile(Players, tiles.getTileLocation(16, 18))
let ghostp = sprites.create(img`
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
    `, SpriteKind.Enemy)
tiles.placeOnTile(ghostp, tiles.getTileLocation(3, 30))
let ghostb = sprites.create(img`
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
    `, SpriteKind.Enemy)
tiles.placeOnTile(ghostb, tiles.getTileLocation(29, 29))
let ghostr = sprites.create(img`
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
    `, SpriteKind.Enemy)
tiles.placeOnTile(ghostr, tiles.getTileLocation(30, 1))
let ghosto = sprites.create(img`
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
    `, SpriteKind.Enemy)
tiles.placeOnTile(ghosto, tiles.getTileLocation(1, 1))
ghostb.follow(Players, 40)
ghosto.follow(Players, 40)
ghostp.follow(Players, 40)
ghostr.follow(Players, 40)
for (let index = 0; index < 200; index++) {
    points = sprites.create(img`
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
        `, SpriteKind.points)
    tiles.placeOnRandomTile(points, assets.tile`transparency16`)
}
if (powerups == 0) {
    game.reset()
} else if (powerups == 1) {
    powerup = sprites.create(img`
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
        `, SpriteKind.Food)
    tiles.placeOnRandomTile(powerup, assets.tile`transparency16`)
    powerup.setKind(SpriteKind.Food)
    controller.moveSprite(Players)
    Players.setVelocity(10, 10)
} else if (powerups == 2) {
    for (let index = 0; index < 2; index++) {
        powerup = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnRandomTile(powerup, assets.tile`transparency16`)
        powerup.setKind(SpriteKind.Food)
    }
    controller.moveSprite(Players)
    Players.setVelocity(10, 10)
} else if (powerups == 3) {
    for (let index = 0; index < 3; index++) {
        powerup = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnRandomTile(powerup, assets.tile`transparency16`)
        powerup.setKind(SpriteKind.Food)
    }
    controller.moveSprite(Players)
    Players.setVelocity(10, 10)
} else {
    game.reset()
}
forever(function () {
    scene.cameraFollowSprite(Players)
})
forever(function () {
    if (pointsnum == 0) {
        game.splash("YOU WIN")
        game.splash("Score" + info.score())
        game.reset()
    }
})
