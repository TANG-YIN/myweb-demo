#!/bin/bash
# 此脚本执行可以同步git-docker目录下的仓库到远端
date=$(date +%y/%m/%d)'同步'
cd /root/git-docker
git add .
git commit -m $date
git push
