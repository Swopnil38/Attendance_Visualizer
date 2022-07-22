import matplotlib.pyplot as plt
import numpy as np

def line_chart(label,value):
    fig = plt.figure(figsize=(18,8))
    y_pos = np.arange(len(label))
    plt.bar(y_pos, value, align='center', alpha=0.5)
    plt.xticks(y_pos, label)
    plt.xticks(rotation = 45)
    return fig

def pie(labels,value):
    print(labels)
    print(value)
    fig, ax = plt.subplots(figsize = (5,5))
    explode = [0.1,0]
    value = np.array(value)
    plt.pie(value,labels=labels,autopct='%1.1f%%',explode=explode,pctdistance=0.85) 
    #draw circle
    centre_circle = plt.Circle((0,0),0.50,fc='white')
    fig2 = plt.gcf()
    fig2.gca().add_artist(centre_circle)
    plt.axis('equal')
    plt.tight_layout()

    return fig