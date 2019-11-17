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
            print("inside snake")
            randomApple(fLs,randAppArgs,extrals)
            return
    if checkBigRect(extrals,rAx,rAy):
        randomApple(fLs,randAppArgs,extrals)
        print("extrals")
        print(extrals)
        print(rAx,rAy)
        return
    if not screenDisplay[0].get_at((rAx+5,rAy+5)) == whiteA:
        randomApple(fLs,randAppArgs,extrals)
        print("here")
    randAppArgs['randAppleX'] = rAx
    randAppArgs['randAppleY'] = rAy
    print(screenDisplay[0].get_at((rAx,rAy)),screenDisplay[0].get_at((rAx+5,rAy+5)))

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
        print(extrals)
        return
    if not screenDisplay[0].get_at((rAx+5,rAy+5)) == whiteA:
        randomApple2(fLs,randA2Args,extrals)
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
    if not screenDisplay[0].get_at((rAx+5,rAy+5)) == whiteA:
        randomAppleSpecial(fLs,randAsArgs,extrals)
    randAsArgs['randAppleXSpecial'] = rAx
    randAsArgs['randAppleYSpecial'] = rAy

def randomAppleE(fLs,randAsArgs,extrals=[]):
    rAx = 0
    rAy = 0
    rAx = random.randrange(0,display_width-block_size,block_size)
    rAy = random.randrange(40,display_height-block_size,block_size)
    for snakePart in fLs:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomAppleE(fLs,randAsArgs,extrals)
            return
    if checkBigRect(extrals,rAx,rAy):
        randomAppleE(fLs,randAsArgs,extrals)
        return
    randAsArgs['randAppleXE'] = rAx
    randAsArgs['randAppleYE'] = rAy

def checkBigRect(rectInfo,rAx,rAy):
    for element in rectInfo:
        if element[0]+element[2] > rAx >= element[0]:
            if element[1]+element[3] > rAy >= element[1]:
                return True
    return False