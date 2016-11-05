import sys
import math
import socket
#//sys.path.append("usr/lib/Leap:/path/to/lib/x86:/path/to/lib")
sys.path.append("C:/Program Files\ (x86)/Leap Motion")
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


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
            data = "m " +str(int(a))+"\n"+ "o " +str(int(b-a)+120)+"\n"+"l " +str(int(br)) + "\n" + "p " + str(int(p))+"\n"
            s.send(data.encode('utf-8'))
            time.sleep(0.3)
       
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

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    s = socket.socket()
    s.connect((str(sys.argv[1]), int(sys.argv[2])))
    main()
    s.close()
