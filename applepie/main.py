import pyglet

window = pyglet.window.Window()

label1 = pyglet.text.Label('Apple Pie',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

label2 = pyglet.text.Label('This is great',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label1.draw()
    label2.draw()

pyglet.app.run()
