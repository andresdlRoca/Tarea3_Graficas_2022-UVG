from gl import Renderer, color, V3, V2

width = 400
height = 400

rend = Renderer(width, height)

rend.glLoadModel("girl.obj",
                 translate = V3(width/2, 10, 0),
                 scale = V3(200,200,200))

rend.glFinish("output.bmp")

