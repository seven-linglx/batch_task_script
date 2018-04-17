# -*- coding: utf-8 -*-
import os
import sys
import subprocess

pcd_dir = sys.argv[1]
vtk_dir = sys.argv[2]
# pcd_dir = '/home/linglx/Data/pcd2vtk/local_laser_pcd'
# vtk_dir = '/home/linglx/Data/pcd2vtk/local_laser_vtk'

pcd_files = []
vtk_files = []

for filename in os.listdir(pcd_dir):
    pcd_files.append(filename)
    vtk_files.append(os.path.splitext(filename)[0] + '.vtk')
    # print(os.path.splitext(filename)[0] + '.vtk')

for i in range(len(pcd_files)):
    print(pcd_files[i], ' ---> ', vtk_files[i])
    src = pcd_dir + '/' + pcd_files[i]
    tar = vtk_dir + '/' + vtk_files[i]
    # print(src, tar)
    # os.system('pcl_pcd2vtk src tar')
    subprocess.call(["pcl_pcd2vtk", src, tar])
