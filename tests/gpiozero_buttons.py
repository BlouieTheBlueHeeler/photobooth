#!/usr/bin/python3

import os
import sys
import time
import logging
import gpiozero

from gpiozero.pins.rpigpio import RPiGPIOFactory

def btn_pressed():
    print('Button was pressed.')

def btn_released():
    print('Button was released.')

def main():
    logging.basicConfig(level=logging.DEBUG)
    print('gpiozero buttons start.')
    logging.info('Start gpiozero buttons test.')

    pin_factory = RPiGPIOFactory()
    pin_19 = pin_factory.pin(19)
    # pin_26 = pin_factory.pin(26)

    pin_19.output_with_state(True)
    # pin_26.input_with_pull(pull='up')

    button_26 = gpiozero.Button(pin=26, pull_up=False)
    button_26.wait_for_press()
    logging.info('Button 26 was pressed.')

    # button_evt_iterations = 1000
    #button_indices = [2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,19,20,21,23,24,25,26,27]
    #button_indices = [19,26]
    #button_objs = {}

    #for idx in button_indices:
    #    button_objs[idx] = gpiozero.Button(idx)
    #    #button_objs[idx].when_pressed = btn_pressed
    #    #button_objs[idx].when_released = btn_released

    #for iter in range(0, button_evt_iterations):
    #    logging.debug('Button event loop: ' + str(iter))
    #    for btn in button_objs.keys():
    #        if button_objs[btn].is_pressed:
    #            logging.debug('Button pressed: ' + str(btn))

    #    time.sleep(0.25)

    logging.info('Finish gpiozero buttons test.')
    print('gpiozero buttons end.')


main()