python attack_main.py ^
-model xception_classifier ^
-eval classification_crossentropy ^
-in ../data/img_data/tench_299.png ^
-tl 0 ^
-min ^
-b 20000 ^
-ps 2 -os 4 ^
-d 0.4 ^
-e 0.05 ^
-r intermediate ^
-m one_fifth ^
-s plus_selection ^
-v 2