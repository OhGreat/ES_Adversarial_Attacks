#!/bin/bash

python attack_main.py \
-model xception_classifier \
-device "cuda:1" \
-eval "crossentropy" \
-dataloader \
-in "/data/shrimps/datasets/one_class/" \
-tl 48 \
-min \
-b 10000 \
-ps 12 -os 50 \
-d 0.9 \
-e 0.02 \
-r "global_discrete" \
-m "individual" \
-s "comma_selection" \
-fp 5 \
-v 2