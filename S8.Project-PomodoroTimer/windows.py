#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2 13:48 2021
Milestone Project: Pomodoro Timer
windows.py
Basically main

@author: lavarius
"""
# boiler plate code to set awareness of process for Windows 10
def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass