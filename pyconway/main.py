import os
import random
import shutil
import sys
from time import sleep

import numpy as np
from numpy._typing import NDArray

WORLD_SIZE = 50

# World methods


def instantiateWorld(size: int):
    return np.zeros((size, size))


def seedWorld(world: NDArray[np.float64]):
    worldShape = world.shape
    row = randBoundedInt((0, worldShape[0] - 1))
    col = randBoundedInt((0, worldShape[1] - 1))
    world[row][col] = 1


def resolveWorld(world, actions):
    for a in actions:
        coords = a[0]
        val = a[1]
        world[coords[0]][coords[1]] = val
    return world


def renderWorld(world: NDArray[np.float64]) -> None:
    terminal_width, terminal_height = shutil.get_terminal_size()
    cell_w = terminal_width // (WORLD_SIZE * 2)
    cell_h = terminal_height // WORLD_SIZE

    lines = []
    for row in world:
        line = ""
        for cell in row:
            char = "██" if cell == 1.0 else "  "
            line += char * max(1, cell_w)
        for _ in range(max(1, cell_h)):
            lines.append(line)

    # Center horizontally
    grid_width = WORLD_SIZE * 2 * max(1, cell_w)
    padding_left = " " * ((terminal_width - grid_width) // 2)

    padded_lines = [padding_left + line for line in lines]
    print("\n".join(padded_lines[:terminal_height]))


# --- Cell methods ---


def resolveCell(
    world: NDArray[np.float64],
    coords: tuple[int, int],
    actions: list[tuple[tuple[int, int], float]],
):
    cellVal: float = world[coords[0]][coords[1]]
    if cellVal == 1.0:
        # North
        if coords[0] > 0:
            neighbour = (coords[0] - 1, coords[1])
            actions.append((neighbour, 1.0))
        # South
        if coords[0] < WORLD_SIZE - 1:
            neighbour = (coords[0] + 1, coords[1])
            actions.append((neighbour, 1.0))
        # East
        if coords[1] < WORLD_SIZE - 1:
            neighbour = (coords[0], coords[1] + 1)
            actions.append((neighbour, 1.0))
        # West
        if coords[1] > 0:
            neighbour = (coords[0], coords[1] - 1)
            actions.append((neighbour, 1.0))
        # Clear self
        selfCoords = (coords[0], coords[1])
        actions.append((selfCoords, 0.0))

    return actions


# --- Plumbing, utility methods ---


def clearTTY():
    os.system("cls" if os.name == "nt" else "clear")  # pyright: ignore[reportUnusedCallResult, reportDeprecated]


def randBoundedInt(bounds: tuple[int, int]):
    return random.randint(bounds[0], bounds[1])


# --- Core loop ---


def getActions(world: NDArray[np.float64]):
    actions = []
    for idxX, r in enumerate(world):
        for idxY, c in enumerate(r):
            resolveCell(world, (idxX, idxY), actions)
    return actions


def loop(world: NDArray[np.float64]) -> None:
    while True:
        actions = getActions(world)
        resolveWorld(world, actions)
        renderWorld(world)
        sleep(0.2)
        clearTTY()


def main():
    world = instantiateWorld(WORLD_SIZE)
    seedWorld(world)
    clearTTY()
    loop(world)


if __name__ == "__main__":
    main()
