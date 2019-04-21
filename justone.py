import numpy as np 
import matplotlib.pyplot as plt 

epoch, loss_train, loss_val = None, None, None
data = [(epoch,1,loss_train,1.5483108,loss_val,1.5472962),
(epoch,2,loss_train,1.5302788,loss_val,1.542648),
(epoch,3,loss_train,1.5132228,loss_val,1.5397749),
(epoch,4,loss_train,1.4974742,loss_val,1.5365001),
(epoch,5,loss_train,1.482971,loss_val,1.533342),
(epoch,6,loss_train,1.4691042,loss_val,1.5315384),
(epoch,7,loss_train,1.455972,loss_val,1.5281217),
(epoch,8,loss_train,1.44311,loss_val,1.5259355),
(epoch,9,loss_train,1.430956,loss_val,1.5238508),
(epoch,10,loss_train,1.4190142,loss_val,1.5210305),
(epoch,11,loss_train,1.4074636,loss_val,1.5182645),
(epoch,12,loss_train,1.3956972,loss_val,1.5160071),
(epoch,13,loss_train,1.3840288,loss_val,1.5123665),
(epoch,14,loss_train,1.3722528,loss_val,1.509065),
(epoch,15,loss_train,1.3598847,loss_val,1.5041443),
(epoch,16,loss_train,1.3478576,loss_val,1.4993694),
(epoch,17,loss_train,1.335649,loss_val,1.4938809),
(epoch,18,loss_train,1.3225068,loss_val,1.4880847),
(epoch,19,loss_train,1.3089892,loss_val,1.481324),
(epoch,20,loss_train,1.2955819,loss_val,1.4730699),
(epoch,21,loss_train,1.2820148,loss_val,1.4643763),
(epoch,22,loss_train,1.2676508,loss_val,1.455802),
(epoch,23,loss_train,1.2535803,loss_val,1.4466741),
(epoch,24,loss_train,1.2391258,loss_val,1.4366047),
(epoch,25,loss_train,1.225245,loss_val,1.4265058),
(epoch,26,loss_train,1.2111247,loss_val,1.4158475),
(epoch,27,loss_train,1.1975657,loss_val,1.4058954),
(epoch,28,loss_train,1.1841817,loss_val,1.3951044),
(epoch,29,loss_train,1.1714486,loss_val,1.3862941),
(epoch,30,loss_train,1.1588717,loss_val,1.3759614)]

here = {'epoch': [k[1] for k in data], 'loss_train': [k[3] for k in data], 'loss_val': [k[5] for k in data]}

print(here)
