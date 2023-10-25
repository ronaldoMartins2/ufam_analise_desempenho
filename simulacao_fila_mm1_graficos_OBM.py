import matplotlib.pyplot as plt

def plot_interval_NBM():
    
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
                ['OBM (ʎ=7, 100%)', 'OBM (ʎ=7, 50%)', 'OBM (ʎ=7, 25%)',
                 'OBM (ʎ=8, 100%)', 'OBM (ʎ=8, 50%)', 'OBM (ʎ=8, 25%)',
                 'SBM (ʎ=9, 100%)', 'SBM (ʎ=9, 50%)', 'SBM (ʎ=9, 25%)',
                 'SBM (ʎ=9.5, 100%)', 'SBM (ʎ=9.5, 50%)', 'SBM (ʎ=9.5, 25%)' ],
                rotation='vertical')
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.3)
    plt.title('Gráfico Comparativo OBM')
    
    plt.axhline(230000, color='red', label='ʎ=7')
    plt.axhline(400000, color='blue', label='ʎ=8')
    plt.axhline(900000, color='green', label='ʎ=9')
    plt.axhline(1900000, color='gray', label='ʎ=9.5')

    plt.legend()

    plot_confidence_interval_values(1, 270068.6848, 262887.5507, 277249.8188, color='red')
    plot_confidence_interval_values(2, 268987.3602, 260804.9496, 277169.7707, color='red')
    plot_confidence_interval_values(3, 274055.4261, 267425.8525, 280684.9997, color='red')

    
    plot_confidence_interval_values(4, 342355.4811, 332927.8094, 351783.1529, color='blue')
    plot_confidence_interval_values(5, 326395.9860, 318349.9089, 334442.0630, color='blue')
    plot_confidence_interval_values(6, 355266.3507, 347813.3404, 362719.3610, color='blue')

    
    plot_confidence_interval_values(7, 411733.1096, 401564.0981, 421902.1211, color='green')
    plot_confidence_interval_values(8, 451344.2472, 441207.5938, 461480.9006, color='green')
    plot_confidence_interval_values(9, 409406.2492, 402872.4325, 415940.0659, color='green')


    plot_confidence_interval_values(10, 447927.8277, 439181.9431, 456673.7124, color='gray')
    plot_confidence_interval_values(11, 431416.6505, 422435.0788, 440398.2222, color='gray')
    plot_confidence_interval_values(12, 464357.7222, 450684.3954, 464357.7222, color='gray')


    #plot_confidence_interval(2, [10, 21, 42, 45, 44])
    #plot_confidence_interval(3, [20, 2, 4, 45, 44])
    #plot_confidence_interval(4, [30, 31, 42, 45, 44])
    #plt.show()
    plt.savefig("output_comparison_interval_plot_obm.png")

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