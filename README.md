# SS-LCD

The core code for the paper *Loop Closure Detection Based on Object-level Spatial Layout and Semantic Consistency*, which has been submitted to TIM 2023.

## Setup

1.1 Ubuntu and ROS

Ubuntu 18.04. ROS Melodic.

1.2 [VisualDet3D](https://github.com/Owen-Liuyuxuan/visualDet3D)

- environment setup

```bash
pip3 install -r requirement.txt
```

- configuration and path setup

Please modify the path and parameters in **visualDet3D/config*.py** files.

- stereo image as input training

```bash
./launchers/det_precompute.sh config/$CONFIG_FILE.py train
./launcher/train.sh  config/$CONFIG_FILE.py 0 $experiment_name
```

- stereo image as input testing

```bash
./launchers/det_precompute.sh config/$CONFIG_FILE.py test
./launchers/eval.sh config/$CONFIG_FILE.py 0 visualDet3D/workdirs/Stereo3D/checkpoint/Stereo3D_latest.pth test
```

- the evaluate results

the object detected results files should be stored in **sequences/xx**. VINS-Fusion could read the results.

1.3 [VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion)

- environment setup

ceres solver: follow [Ceres Installation](http://ceres-solver.org/installation.html)

- an example

```bash
 roslaunch vins vins_rviz.launch
  rosrun vins kitti_odom_test ~/catkin_ws/src/VINS-Fusion/config/kitti_odom/kitti_config00-02.yaml YOUR_DATASET_FOLDER/sequences/00/
```

1.4 Spatial layout difference computing

With the object detection results and pose estimation results, you can test your own loop detection and store its results as two files, such as **graph1.txt, graph2.txt**. To compute the graphs edit distance, you can run:

```bash
./SL path_to_graph1/graph1.txt path_to_graph2/graph2.txt
```

The executable program will output the matched nodes with minimum distance between graph1 and graph2.

## Notes

We are recently busy with review comments and revisions to the paper. The whole system for our paper will be released soon in this page.

## Related Paper:

if you think the repository and codes are useful, please cite the following papers.

```bash
@ARTICLE{9327478,
  author={Y. {Liu} and Y. {Yuan} and M. {Liu}},
  journal={IEEE Robotics and Automation Letters}, 
  title={Ground-aware Monocular 3D Object Detection for Autonomous Driving}, 
  year={2021},
  doi={10.1109/LRA.2021.3052442}}
  
@article{qin2019fusion,
  author={Tong Qin and Jie Pan and Shaozu Cao and Shaojie Shen},
  title={A General Optimization-based Framework for Local Odometry Estimation with Multiple Sensors},
  journal={ArXiv},
  year={2019},
  volume={abs/1901.03638}}
```