import matplotlib.pyplot as plt

def plot_interval_NBM():
    
    plt.xticks([1, 2, 3, 4], 
                ['STS/AREA (ʎ=7)', 'STS/AREA (ʎ=8)', 'STS/AREA (ʎ=9)', 'STS/AREA (ʎ=9.5)' ],
                rotation='vertical')
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.3)
    plt.title('Gráfico Comparativo STS/AREA')
    
    plt.axhline(230000, color='red', label='ʎ=7')
    plt.axhline(400000, color='blue', label='ʎ=8')
    plt.axhline(900000, color='green', label='ʎ=9')
    plt.axhline(1900000, color='gray', label='ʎ=9.5')

    plt.legend()

    plot_confidence_interval_values(1, 60024758.2857, 165021535637.34296, -164901486120.77155, color='red')
    plot_confidence_interval_values(2, 181462550.1666, 88582659132.03305, -88219734031.6997, color='blue')
    plot_confidence_interval_values(3, 90973599.3095, 63657253019.86305, -63475305821.244, color='green')
    plot_confidence_interval_values(4, 519008283.5714, 809466169403.7822, -808428152836.6394, color='gray')
    #plot_confidence_interval_values(4, 607900553.761, 1947269149507.579, -1946053348400.0552, color='red')

    #plot_confidence_interval(2, [10, 21, 42, 45, 44])
    #plot_confidence_interval(3, [20, 2, 4, 45, 44])
    #plot_confidence_interval(4, [30, 31, 42, 45, 44])
    #plt.show()
    plt.savefig("output_comparison_interval_plot_sts_area.png")

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