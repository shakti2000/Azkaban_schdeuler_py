# Azkaban Scheduler Script for EMR Cluster

## Overview

This Python script automates the scheduling of jobs on an Azkaban instance, specifically designed to address the issue faced by EMR clusters that are manually scaled. In the past, we used to restart the EMR cluster every Sunday for health checks, but this resulted in all scheduled Azkaban jobs being deleted. This script solves that problem by scheduling jobs after the cluster restart. The script is made for a single schedule but you can modify it easily to perform it for multiple schedules at once

## Features

- Automatically reschedules Azkaban jobs after an EMR cluster restart.
- Handles job scheduling using Python and Azkaban's API.
- Can be scheduled to run on specific days or triggered based on your needs.
- Customizable to meet specific job scheduling needs for your environment.

## Requirements

- Python 3
- Azkaban server with accessible API endpoints
- Boto3 for interacting with AWS EMR (if applicable)
- knowledge on cron jobs and azkaban APIs

