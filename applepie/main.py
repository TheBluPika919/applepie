import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('Graphics/logo.png')

label1 = pyglet.text.Label('Apple Pie',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

label2 = pyglet.text.Label('This is great',
                          font_name='Times New Roman',
                          font_size=72,
                          color=(255, 255, 0, 255),
                          x=window.width//2, y=0,
                          anchor_x='center', anchor_y='bottom')


from pyglet.gl import *
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

pos = [0,20]

@window.event
def on_draw():
    window.clear()
    label1.draw()
    label2.draw()
    image.blit(
        window.width//2-image.width//2+pos[0],
        window.height//2-image.width//2+pos[1])

from pyglet.window import key

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        pos[1] += 10
    elif symbol == key.DOWN:
        pos[1] -= 10
    elif symbol == key.LEFT:
        pos[0] -= 10
    elif symbol == key.RIGHT:
        pos[0] += 10

pyglet.app.run()
