#!/usr/bin/env python
import os

def clback():
  try :
    os.system('mntnex')
    red()
  except :
    os.system('umntnex')
    clback()

def red():
  try:
	

	
