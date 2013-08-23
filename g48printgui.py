#!/usr/bin/env python
# Pygame GUI for displaying the output of an HP50G graphing calculator.
#
# Copyright 2013 Travis Goodspeed

from Good48 import *;
import pygame, sys, math, time, os, inspect;
import thread, time;

from pygame.locals import *;

BGCOLOR=(0,0,0xFF);
INKCOLOR=(0xFF,0xFF,0xFF);



calc=Good48();


class PrinterView(pygame.sprite.Sprite):
    """View of the printer's output tape."""

    x=0;
    y=0;
    def clear(self):
        """Clears the display."""
        self.image.fill(BGCOLOR);
        self.x=0;
        self.y=0;
        
    def reset(self):
        print "I forgot to hook reset().";
    def selftest(self):
        print "I forgot to hook selftest().";
    def drawchar(self,c):
        sys.stdout.write("%c" % c);
    def drawcol(self,char):
#        print "I should paint %02x as image data." % char;
        for r in range(0,8):
            b=(1<<r);
            x=self.x;
            y=self.y;
            if char&b>0:
                pygame.draw.line(self.image,
                             INKCOLOR,
                             (2*x+1,2*y+2*r),
                             (2*x+1,2*y+2*r+1));
                pygame.draw.line(self.image,
                             INKCOLOR,
                             (2*x,2*y+2*r),
                             (2*x,2*y+2*r+1));
        self.x=self.x+1;
    def lfgraph(self):
        print "I should do a graphical newline.";
    def lftext(self):
        self.x=0;
        self.y=self.y+8;


    def __init__(self,width=640,height=480):
        self.printer=Good48Printer(self);
        pygame.sprite.Sprite.__init__(self);
        self.width=width;
        self.height=height;
        self.image=pygame.Surface([width,height]);
        #self.image=pygame.image.frombuffer(self.pbm,[width,height],"RGB");
        self.clear();
    def drawdata(self):
        """Draws the printed image to the screen."""
        pass;
    def updatedatathread(self,repeat=True,doodad=True):
        """Updates in the background."""
        while 1:
            self.updatedata(threaded=True);
    def updatedata(self,threaded=False,doodad=False):
        """Updates the view by querying the DB."""
        bs=calc.read(1);
        self.printer.handle(bs);

class PrinterGame:
    printerview=None;
    def __init__(self,width,height):
        """Initializes the SasaCommander window."""
        pygame.init();
        self.screen=pygame.display.set_mode((width,height),
                                            #(self.width,self.height),
                                            pygame.RESIZABLE);
        width, height=self.screen.get_size();
        self.width=width;
        self.height=height;
        
        self.printerview=PrinterView(width,height);

        pygame.display.set_caption('HP82240B Emulator');
    def MainLoop(self):
        thread.start_new_thread( self.printerview.updatedatathread, (self.printerview,True) )
        while True:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit();
                if event.type == KEYDOWN:
                    self.keypressed(event.key);

            pygame.display.update();
            self.printerview.drawdata();
            self.screen.blit(self.printerview.image,
                             (0,0));
            pygame.display.flip();
    def keypressed(self,key):
        """Handler for key presses."""
        if key==K_c:
            self.printerview.clear();
if __name__ == "__main__":
    MainWindow = PrinterGame(800,420)
    MainWindow.MainLoop()

