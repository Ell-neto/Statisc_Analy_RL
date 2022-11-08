# Instructions to use the code 💻

The plots below are from three different datasets, named data1 the [Dados_Iz](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/data/Dados_Iz.xlsx), data2 (for input power [2.45Pth](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/data/PPth245.xlsx)) and data3 (for input power [3.6mJ](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/data/3.6mJ.xlsx)).  

In the **Class Opers**, we have two functions:  
- In function deltait, there is only a single parameter:  

        data - Please inform data as arrays  
The return is an n-dimensional array normalized by m-lines.

- In function mat_norm, two parameters must be entered:

        data - Please inform data as arrays
        
        med - None (default). If True, the outcome is a matriz normalized using the function deltait.
We obtain two returns, the first named "a" and the second named "b". Outcome "a" is normalized and is used to plot a heatmap, whereas return "b" gives Parisi histogram.           


In **Class GrafsIzra**, we have only one function (fit_izra), since it is dedicated to fits of the emittd intensities using the Izrailev PDF, with parameters::  

        data - Please inform data as arrays
        
        model - Some functions determined from Izrailev PDF (Izrailev model), with options 'izrailev4', 'izrailev6', 'izrailev8' and 'izrailev10'
        
        density - True or False
        
        color1 - Color of the histogram, using the colors available from matplotlib in https://matplotlib.org/stable/gallery/color/named_colors.html
        
        color2 - Color of the function, using the colors available from matplotlib in https://matplotlib.org/stable/gallery/color/named_colors.html
        
        title - Inform which model you chose, for example, if you chose izrailev4, just put the "4" here, which will be added to the title.
        
        glog - None (default). If True, it creates a scatter of the histogram + function with log-log axes.
        
The function has two returns: the parameters of the Izrailev model and a covariance matrix (error). Below we used data1 and the model 'Izrailev4':  
![par_error](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/params_error.png)  
Here is the plot of the outcome for the Izrailev model in case glog is None (📊+📈).  
![grafa1](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_1a.png)
![grafb1](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/Figure_2a.png)  
If glog is True, the outcome of Izrailev model is plotted in log-log scale:  
![grafa2](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/fig1b.png)
![grafb2](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/fig2b.png)  
Note: the plot in log-log scale used the same data as the plot in linear-linear scale.   

In **Class GrafsVar**, we have four functions, as follows:
- Function sohist, which is a standard histogram 📊, with parameters:  

        data - Please inform data as arrays
        
        density - True or False
        
        color - Color of the histogram, using the colors available from matplotlib in https://matplotlib.org/stable/gallery/color/named_colors.html
        
        title - Plot title   
Using data3, with the second return of function mat_norm, we plot Parisi histogram:  
![hist_parisi](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/36_histoparisi.png)

- Function varii, which gives an estimate of the range of maximum intensity from the data 📈, with parameters:

        data - Please inform data as arrays
        
        color - Color of the function, using the colors available from matplotlib in https://matplotlib.org/stable/gallery/color/named_colors.html
        
        vall - In case one wishes to have an initial range for the plot (useful in case of very large datasets)
        
        title - Plot title  
 Using data2, the following plot is obtained:    
 ![varii](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/intens_max.png)  
 Note: This function also has a return, which uses the mat_norm function to calculate it, however, the data is not with the application of deltait.
 
 - Function grafs_a plots a 3D graph. It is important to note that it has an return (set to estimate the range of intensity used to generate the plot) that is a random value chosen for the intensity (using randint). The parameters are:
        
        data - Please inform data as arrays
        
        color - Choose the colormap, available in https://matplotlib.org/stable/tutorials/colors/colormaps.html
        
        title - Plot title 

        titlex - Label of x-axis

        titley - Label of y-axis
     
        titlez - Label of z-axis
        
Using data3, we obtain the following plot:    
![graf36](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/3d_36g.png)
Using another dataset, we obtain:   
![gra56](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/fig56.png)  
Note: we recall that the spectrum number is 1000.  

- Function ht_map provides a heatmap for the plot of Pearson correlation coeffcient. The parameters are:

        data - Please inform data
        
        cmap - Choose the colormap, available in https://matplotlib.org/stable/tutorials/colors/colormaps.html
        
        title - Plot title 

        titlex - Label of x-axis

        titley - Label of y-axis
     
Using data3, and recalling that we make use of the first return of function mat_norm, we obtain the heatmap:    
![graf36map](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/36_mapcalor.png)  

Using another dataset, we obtain:   
![map47](https://github.com/Ell-neto/Statisc_Analy_RL/blob/master/Instruction/img/mp_cal47.png)  


*Last note: all plots are set to treat a given dataset. If your data have many figures or are too large, you should adjust main.py conveniently. In case of any doubt, do not hesitate in contacting [us✉️](mailto:manoelfsneto@live.com).*
