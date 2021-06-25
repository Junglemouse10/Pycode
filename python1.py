from mcpi.minecraft import Minecraft
from mcpi import block

ip = "10.183.3.20"
mc = Minecraft.create(ip, 4711)
#mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(-23.1,2.0,60.1)
# CLEAR AN AREA WITH AIR TO BUILD
#256 x 256 x 128 blocks.
air = 0
#mc.setBlocks(start x, start y,start z , end x ,end y, end z,air) # clear some air        
mc.setBlocks(48.5,0.0 ,8.9,-47.6,-5,116.9,98) # clear some air                                               
x, y, z = mc.player.getPos()
mc.setBlocks(0,62,0,35,3)
#mc.player.setPos(-10.5,1,69.7)     #Player Postion

mc.setBlocks(127.7, 0, -127.7,-127.7,55,127.7,air)
mc.setBlocks(-18, 0, 54, -29, 0, 65, 89)
mc.setBlocks(-18,1,54,-29,1,54,155)
mc.setBlocks(-18,2,54,-29,2,54,155)
mc.setBlocks(-29,1,65,-29,2,54,155)
mc.setBlocks(-28,2,65,-18,1,65,155)
mc.setBlocks(-18,1,64,-18,2,55,155)
mc.setBlocks(-19,2,55,-28,1,64,8)
