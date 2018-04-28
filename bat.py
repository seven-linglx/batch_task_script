# -*- coding: utf-8 -*-
import os
import sys
import subprocess

# pcd_dir = '/home/linglx/Data/pcd2vtk/local_laser_pcd'
# vtk_dir = '/home/linglx/Data/pcd2vtk/local_laser_vtk'

for i in range(40):
    cur = "--poles_cur_path=/home/linglx/Data/poles/" + str(i) + "poles_cur.csv"
    map = "--poles_map_path=/home/linglx/Data/poles/" + str(i) + "poles_map.csv"
    pose = "--pose_path=/home/linglx/Data/poles/" + str(i) + "pose.csv"

    #  print(cur, map, pose)
    subprocess.call([
        "/home/linglx/CLionProjects/Projects/cmake-build-release/hungarian_matcher/HungarianMatcher",
        cur, map, pose
    ])
    #  subprocess.call(["python /home/linglx/PycharmProjects/gui/show_poles.py", i])
    os.popen('python /home/linglx/PycharmProjects/gui/show_poles.py ' + str(i))
