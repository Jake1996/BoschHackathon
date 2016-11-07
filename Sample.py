import sys
import math
import socket
import os
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from threading import Thread
sys.path.append("C:/Program Files\ (x86)/Leap Motion")

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
		while True :
			foo(self.impl())

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print type(ch)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

class SampleListener(Leap.Listener):
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        pass
    def on_connect(self, controller):
        pass
    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        pass
    def on_exit(self, controller):
        pass
    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
       
        # Get hands
        for hand in frame.hands:
            # Get arm bone
            arm = hand.arm
            x1 = arm.wrist_position[0]
            y1 = arm.wrist_position[1]
            z1 = arm.wrist_position[2]
            
            x2 = arm.elbow_position[0]
            y2 = arm.elbow_position[1]
            z2 = arm.elbow_position[2]

            #bone = Leap.Bone()
            #print(bone.basis)
            
            x3 = y3 = z3 = 0
            thumbx = thumby = thumbz = 0
            p=0
            for fingers in hand.fingers:
                if fingers.type == 0:
                    thumbx = fingers.tip_position[0]
                    thumby = fingers.tip_position[1]
                    thumbz = fingers.tip_position[2]
                elif fingers.type == 2:
                    x3 = fingers.tip_position[0]
                    y3 = fingers.tip_position[1]
                    z3  = fingers.tip_position[2]
                
            #midfingangle = math.degrees(math.atan((y3-y1)/(z1-z3)))
            #thumbangle = math.degrees(math.atan((thumby-y1)/(z1-thumbz)))
            
            #print("Midfing & Thumb",midfingangle-thumbangle)
            #print("Arm directionv" + str(arm.direction))
            #print()
            v1=(x3-x1,y3-y1,z3-z1)
            v2=(thumbx-x1,thumby-y1,thumbz-z1)
            v3=sum(p*q for p,q in zip(v1, v2))
            v3=v3/(math.sqrt(v1[0]**2+v1[1]**2+v1[2]**2)*math.sqrt(v2[0]**2+v2[1]**2+v2[2]**2))
            p=(1-v3)*90*1.5
            if(p>90):
                p=90
            a = math.degrees(math.atan((arm.direction[1]/(-arm.direction[2]))*1.2)) + 30
            if(a<30):
                a=30
            b = math.degrees(math.atan((y3-y2)/(z2-z3)))
            br=math.degrees(math.atan(-(arm.direction[0]/arm.direction[2])*1.2)) + 90
            
            p = int(p)     #claw angle
            p = p*0.66
            p = 180 - p

            a = a - 30     #ankle angle
            a = a*1.2

            br = 180-br    # base rotation

            data = "m " +str(int(a))+"\n"+ "o " +str(int((int(b-a)+70)*2))+"\n"+"l " +str(int(br)) + "\n" + "p " + str(int(p))+"\n"
            #o = ((b-a)+90)

            # print data
            sender(data)
            time.sleep(0.25)
       
        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ""

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"
s = socket.socket()
s.connect((str(sys.argv[1]), int(sys.argv[2])))
controller = ""
listener = ""
var = True
file_name = "record.txt"
#raw_input('enter filename to save into :') + ".txt"
f = open(file_name,'w')
def foo(n):
    global controller
    global listener
    if n=="q" :
        s.close()
        global var
        var = False
        controller.remove_listener(listener)
        sys.exit()
    sender(n+"\n")
    print n

def sender(data) :
    global s
    global f
    print data
    s.send(data.encode('utf-8'))
    f.write(data)
def main():
    global controller
    global listener
    t = Thread(target=getch)
    t.start()
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press q to quit"
    global var
    while var:
        pass
getch = _Getch()
if __name__ == "__main__":
    main()
