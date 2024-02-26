import screenbuffer
import world


def update():
    screenbuffer.clear(96)
    screenbuffer.write_at(world.player_x + world.player_y * screenbuffer.CELL_COLUMNS, "@"         )
