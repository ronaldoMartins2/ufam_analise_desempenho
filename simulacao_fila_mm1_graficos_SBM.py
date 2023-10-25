import matplotlib.pyplot as plt

def plot_interval_NBM():
    
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
                ['SBM (ʎ=7, s=0)', 'SBM (ʎ=7, s=1)', 'SBM (ʎ=7, s=2)', 'SBM (ʎ=7, s=3)', 'SBM (ʎ=7, s=4)',
                 'SBM (ʎ=8, s=0)', 'SBM (ʎ=8, s=1)', 'SBM (ʎ=8, s=2)', 'SBM (ʎ=8, s=3)', 'SBM (ʎ=8, s=4)',
                 'SBM (ʎ=9, s=0)', 'SBM (ʎ=9, s=1)', 'SBM (ʎ=9, s=2)', 'SBM (ʎ=9, s=3)', 'SBM (ʎ=9, s=4)',
                 'SBM (ʎ=9.5, s=0)', 'SBM (ʎ=9.5, s=1)', 'SBM (ʎ=9.5, s=2)', 'SBM (ʎ=9.5, s=3)', 'SBM (ʎ=9.5, s=4)' ],
                rotation='vertical')
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.3)
    plt.title('Gráfico Comparativo SBM')
    
    plt.axhline(230000, color='red', label='ʎ=7')
    plt.axhline(400000, color='blue', label='ʎ=8')
    plt.axhline(900000, color='green', label='ʎ=9')
    plt.axhline(1900000, color='gray', label='ʎ=9.5')

    plt.legend()

    plot_confidence_interval_values(1, 269172.7076, 228160.3513, 310185.0639, color='red')
    plot_confidence_interval_values(2, 257409.5525, 222544.3247, 292274.7803, color='red')
    plot_confidence_interval_values(3, 238952.6221, 208857.2273, 269048.0169, color='red')
    plot_confidence_interval_values(4, 268316.0884, 225731.2767, 310900.9000, color='red')
    plot_confidence_interval_values(5, 243393.1301, 210477.8268, 276308.4334, color='red')

    
    plot_confidence_interval_values(6, 352690.5203, 282487.7414, 422893.2991, color='blue')
    plot_confidence_interval_values(7, 293226.5688, 250067.2228, 336385.9148, color='blue')
    plot_confidence_interval_values(8, 305159.1430, 263855.6443, 346462.6417, color='blue')
    plot_confidence_interval_values(9, 308381.7944, 269740.7919, 347022.7970, color='blue')
    plot_confidence_interval_values(10, 288208.0852, 248414.3090, 328001.8614, color='blue')

    
    plot_confidence_interval_values(11, 404736.7616, 364911.1569, 444562.3663, color='green')
    plot_confidence_interval_values(12, 403161.2086, 357089.4770, 449232.9402, color='green')
    plot_confidence_interval_values(13, 391125.0913, 341866.0406, 440384.1420, color='green')
    plot_confidence_interval_values(14, 405369.9635, 352872.1703, 457867.7567, color='green')
    plot_confidence_interval_values(15, 397696.4859, 340258.6434, 455134.3285, color='green')


    plot_confidence_interval_values(16, 450289.3687, 424269.1781, 476309.5593, color='gray')
    plot_confidence_interval_values(17, 465614.5244, 410502.8349, 520726.2139, color='gray')
    plot_confidence_interval_values(18, 413404.6657, 356046.8092, 470762.5221, color='gray')
    plot_confidence_interval_values(19, 443000.9838, 387335.1426, 498666.8249, color='gray')
    plot_confidence_interval_values(20, 414910.5998, 361493.5436, 468327.6559, color='gray')


    #plot_confidence_interval(2, [10, 21, 42, 45, 44])
    #plot_confidence_interval(3, [20, 2, 4, 45, 44])
    #plot_confidence_interval(4, [30, 31, 42, 45, 44])
    #plt.show()
    plt.savefig("output_comparison_interval_plot_sbm.png")

def plot_confidence_interval_values(x, mean, top, bottom, color, horizontal_line_width=0.25):
    #mean = statistics.mean(values)
    #stdev = statistics.stdev(values)
    
    left = x - horizontal_line_width / 2
    #top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    #bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color)
    plt.plot([left, right], [top, top], color=color)
    plt.plot([left, right], [bottom, bottom], color=color)
    #plt.plot(x, mean, 'o', color='#f44336')
    plt.plot(x, mean, 'o', color=color)

    return mean #, confidence_interval


plot_interval_NBM()