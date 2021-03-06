# GameOfLife

<p align="center">
<img src="https://github.com/SRingshandl/GameOfLife/blob/main/GoL_animation.gif" width="30%">
</p>

Outputs a video file of Conway's Game of Life.   
You can specify board size and live cell number (randomized position).  

Conway's game of life has the following rules:  
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.  
2. Any live cell with two or three live neighbours lives on to the next generation.  
3. Any live cell with more than three live neighbours dies, as if by overpopulation.  
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.  

In this version the bordering cells are set to permanent dead. So this is a version of the game without a toroidal array.

For further information see: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
