class Config():
	FPS = 15
	MENU_FPS = 60
	CELLSIZE = 20
	WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
	assert (WINDOW_WIDTH % CELLSIZE == 0), 'should be an integer multiple of cellsize'
	assert (WINDOW_HEIGHT % CELLSIZE == 0), 'should be an integer multiple of cellsize'
	CELL_WIDTH = int(WINDOW_WIDTH/CELLSIZE)
	CELL_HEIGHT = int(WINDOW_HEIGHT/CELLSIZE)
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	DARKGREEN = (0, 155, 0)
	GREY = (25, 25, 25)
	BACKGROUND_COLOR = BLACK
	GRIDCOLOR = GREY