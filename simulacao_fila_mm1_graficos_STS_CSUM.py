import matplotlib.pyplot as plt

def plot_interval_NBM():
    
    plt.xticks([1, 2, 3, 4], 
                ['STS/CSUM (ʎ=7)', 'STS/CSUM (ʎ=8)', 'STS/CSUM (ʎ=9)', 'STS/CSUM (ʎ=9.5)' ],
                rotation='vertical')
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.3)
    plt.title('Gráfico Comparativo STS/CSUM')
    
    plt.axhline(230000, color='red', label='ʎ=7')
    plt.axhline(400000, color='blue', label='ʎ=8')
    plt.axhline(900000, color='green', label='ʎ=9')
    plt.axhline(1900000, color='gray', label='ʎ=9.5')

    plt.legend()

    plot_confidence_interval_values(1, 41513045.9285, 1670240114821.357, -1670157088729.5, color='red')
    plot_confidence_interval_values(2, 33744502.9761, 4656043206416.432, -4655975717410.479, color='blue')
    plot_confidence_interval_values(3, 237525567.761, 5291419117982.037, -5290944066846.514, color='green')
    plot_confidence_interval_values(4, 162844001.8095, 4728794447279.537, -4728468759275.918, color='gray')
    

    #plot_confidence_interval(2, [10, 21, 42, 45, 44])
    #plot_confidence_interval(3, [20, 2, 4, 45, 44])
    #plot_confidence_interval(4, [30, 31, 42, 45, 44])
    #plt.show()
    plt.savefig("output_comparison_interval_plot_sts_csum.png")

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