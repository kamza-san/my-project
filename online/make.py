import pygame
import socket
import threading
import sys
import time
import random
import socket
from pygame.locals import *
from offline.player import Player
from offline.object import Object
from offline.button import Button
from offline.map import generate_map,touch,touch_side,touch_near
import json
from image import scoreimage,background,player_right,player_left
objects = []

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                coords = msg.split("]")[-1].strip()
                a, b = map(int, coords.split(","))
                enemy.x = a
                enemy.y = 550 + score - b
            else:
                break
        except:
            break

def make(clock,screen,FPS,MAX_WIDTH,MAX_HEIGHT,MYFONT):
    host = "192.168.10.25"
    port = 20002
    
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((host, port))
    except TimeoutError:
        print("서버에 연결할 수 없습니다. (TimeoutError 발생)")
        pygame.quit()
        sys.exit()
    except Exception as e:
        print(f"서버 연결 중 오류가 발생했습니다: {e}")
        pygame.quit()
        sys.exit()

    print("서버에 연결되었습니다.(Ctrl+C로 종료)")

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True
    receive_thread.start()

    global out
    out = True
    level = "hard"
    game(clock,screen,FPS,MAX_WIDTH,MAX_HEIGHT,MYFONT,level)

def player_gravity(a):
    for obj in objects:
        obj.up(a)
    lava.up(a)
    global high
    global m
    global score
    high += a
    m += a
    score += a

def say(player: Player):
    msg = str(player.x)+","+str(score)
    try:
        client.send(msg.encode())
    except KeyboardInterrupt:
        print("\n[!] 클라이언트를 종료합니다.")
        client.close()
        pygame.quit()
        sys.exit()

def game(clock,screen,FPS,MAX_WIDTH,MAX_HEIGHT,MYFONT,level):
    global player
    global score
    global high
    global m
    global enemy
    global lava
    srv_timer = 0
    enemy = Player(MAX_WIDTH//2-30,MAX_HEIGHT-250,1,player_right,player_left,screen)
    score = -10
    if level == "easy":
        speed = -1
    elif level == "normal":
        speed = -2
    else:
        speed = -4
    score = -10
    player = Player(MAX_WIDTH//2-30,MAX_HEIGHT-250,1,player_right,player_left,screen)
    objects.append(Object(0, 600, 600, 300, 255,255,0,screen))
    lava = Object(0,800,600,800,255,127,0,screen)
    scoreboard = Button(40,40,200,80,scoreimage,str(score)+"cm",MYFONT,225,225,107,screen)
    if_jump = False
    second_jump = False
    high = -800
    m = 600
    jump_speed = 5
    while True:
        srv_timer += 1
        if srv_timer >= 3:
            say(player)
            srv_timer = 0
        right = True
        left = True
        high = high % 1600 
        screen.blit(background,(0,high+1600))
        screen.blit(background,(0,high))
        screen.blit(background,(0,high-1600))
        clock.tick(FPS)
        if jump_speed >= -20:
            jump_speed -= 1
        for obj in objects: 
            if touch_side(player,obj) == "top" or touch_near(player,obj) == "top" or (touch_side(player,obj) == "left" and jump_speed < 0) or (touch_side(player,obj) == "right" and jump_speed < 0):
                jump_speed = 0
                if_jump = True
                second_jump = False
                a = player.y - obj.y + 60
                for obj in objects:
                    obj.up(a)
                lava.up(a)
                high += a
                m += a
                score += a
                break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_k:
                    if if_jump:
                        jump_speed = 25
                        if_jump = False
                        second_jump = True
                    elif second_jump:
                        jump_speed = 20
                        second_jump = False
                if event.key == pygame.K_s:
                    jump_speed = -20
        pressed_keys = pygame.key.get_pressed()
        player_gravity(jump_speed)
        for obj in objects:
            if touch_near(player,obj) == "right":
                left = False
            elif touch_near(player,obj) == "left":
                right = False
            elif touch(player,obj) and jump_speed > 0:
                jump_speed = 0
                a = player.y - obj.y - obj.si_y
                for obj in objects:
                    obj.up(a)
                lava.up(a)
                high += a
                m += a
                score += a     
                break
        player.move(pressed_keys,right,left)
        lava.up(speed)
        if player.get_rect().colliderect(lava.get_rect()):
            print("닿음;;")
        if len(objects) != 0:
            if lava.y <= objects[0].y:
                del objects[0]
        if m >= 0:
            m -= 180
            x = 0
            width = 100
            height = 40
            objects.append(Object(x,m,width,height,255,255,0,screen))
        scoreboard.text = str(score)+"cm"
        for obj in objects:
            obj.draw()
        player.draw()
        lava.draw()
        scoreboard.draw()
        pygame.display.update()