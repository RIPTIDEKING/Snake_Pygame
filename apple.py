import random

from resorces_basic import *

def randomApple(ls,randAppArgs):
    #global randAppleX,randAppleY,countApple
    randAppArgs['countApple'] += 1
    rAx = 0
    rAy = 0
    rAx = round(random.randrange(0,display_width-block_size,block_size)/block_size)*block_size
    rAy = round(random.randrange(0,display_height-block_size,block_size)/block_size)*block_size
    for snakePart in ls:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomApple(ls,randAppArgs)
            print(len(ls))
            return
    randAppArgs['randAppleX'] = rAx
    randAppArgs['randAppleY'] = rAy

def randomApple2(ls,randA2Args):
    #global randAppleX2,randAppleY2
    rAx = 0
    rAy = 0
    rAx = round(random.randrange(0,display_width-block_size,block_size)/block_size)*block_size
    rAy = round(random.randrange(0,display_height-block_size,block_size)/block_size)*block_size
    for snakePart in ls:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomApple2(ls,randA2Args)
            return
    randA2Args['randAppleX2'] = rAx
    randA2Args['randAppleY2'] = rAy
    
def randomAppleSpecial(ls,randAsArgs):
    #global randAppleXSpecial,randAppleYSpecial
    rAx = 0
    rAy = 0
    rAx = round(random.randrange(0,display_width-block_size,block_size)/block_size)*block_size
    rAy = round(random.randrange(0,display_height-block_size,block_size)/block_size)*block_size
    for snakePart in ls:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomAppleSpecial(ls,randAsArgs)
            return
    randAsArgs['randAppleXSpecial'] = rAx
    randAsArgs['randAppleYSpecial'] = rAy