import random

from resorces_basic import *

def randomApple(fLs,randAppArgs,extrals = []):
    randAppArgs['countApple'] += 1
    rAx = 0
    rAy = 0
    rAx = random.randrange(0,display_width-block_size,block_size)
    rAy = random.randrange(40,display_height-block_size,block_size)
    for snakePart in fLs:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomApple(fLs,randAppArgs,extrals)
            return
    if checkBigRect(extrals,rAx,rAy):
        randomApple(fLs,randAppArgs,extrals)
        return
    randAppArgs['randAppleX'] = rAx
    randAppArgs['randAppleY'] = rAy

def randomApple2(fLs,randA2Args,extrals = []):
    rAx = 0
    rAy = 0
    rAx = random.randrange(0,display_width-block_size,block_size)
    rAy = random.randrange(40,display_height-block_size,block_size)
    for snakePart in fLs:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomApple2(fLs,randA2Args,extrals)
            return
    if checkBigRect(extrals,rAx,rAy):
        randomApple2(fLs,randA2Args,extrals)
        return
    randA2Args['randAppleX2'] = rAx
    randA2Args['randAppleY2'] = rAy
    
def randomAppleSpecial(fLs,randAsArgs,extrals=[]):
    rAx = 0
    rAy = 0
    rAx = random.randrange(0,display_width-block_size,block_size)
    rAy = random.randrange(40,display_height-block_size,block_size)
    for snakePart in fLs:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomAppleSpecial(fLs,randAsArgs,extrals)
            return
    if checkBigRect(extrals,rAx,rAy):
        randomAppleSpecial(fLs,randAsArgs,extrals)
        return
    randAsArgs['randAppleXSpecial'] = rAx
    randAsArgs['randAppleYSpecial'] = rAy

def checkBigRect(rectInfo,rAx,rAy):
    for element in rectInfo:
        if element[0]+element[2] > rAx >= element[0]:
            if element[1]+element[3] > rAy >= element[1]:
                return True
    return False