#!/bin/bash
cat requirements.txt | xargs sudo apt remove -y
sudo apt autoremove
