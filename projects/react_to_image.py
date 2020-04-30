#!/usr/bin/env python3

import time

import anki_vector
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes

def handle_object(robot, event_type, event):
    robot.behavior.say_text("Found you!")

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial,
                           default_logging=False,
                           show_viewer=True,
                           behavior_control_level=anki_vector.connection.ControlPriorityLevel.OVERRIDE_BEHAVIORS_PRIORITY,
                           enable_custom_object_detection=True) as robot:
        robot.events.subscribe(handle_object, anki_vector.events.Events.object_appeared)

        wall_obj = robot.world.define_custom_wall(custom_object_type=CustomObjectTypes.CustomType02,
                                                  marker=CustomObjectMarkers.Diamonds4,
                                                  width_mm=60,
                                                  height_mm=60,
                                                  marker_width_mm=50,
                                                  marker_height_mm=50,
                                                  is_unique=True)
        if wall_obj is not None:
            print("All objects defined successfully!")
        else:
            print("One or more object definitions failed!")
            return

        print("\n\nReady to recognise the object")

        try:
            while True:
                time.sleep(20)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
