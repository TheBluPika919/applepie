import pyglet

window = pyglet.window.Window()

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
@window.event
def on_draw():
    window.clear()
    label1.draw()
    label2.draw()

pyglet.app.run()
