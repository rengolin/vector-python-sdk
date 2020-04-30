import time

import anki_vector
from anki_vector.events import Events
from anki_vector.util import degrees

def new_face(robot, event_type, event):
    robot.behavior.say_text("Do I know you?")
    for face in robot.world.visible_faces:
        robot.behavior.say_text(f"Are you {face.name}? or...")
        print(f"{face.name}")
    robot.behavior.say_text("whatever...")


with anki_vector.Robot(enable_face_detection=True) as robot:
    robot.events.subscribe(new_face, Events.robot_changed_observed_face_id)

    print("------ show vector your face, press ctrl+c to exit early ------")
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        robot.disconnect()
