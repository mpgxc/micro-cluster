from collections import Counter
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def make_cloud(text):
    wordcloud = WordCloud(max_font_size=100, width=1520, height=535).generate(text)
    plt.figure(figsize=(16, 9))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


objects = []
performance = []
limit = 15
count = 0
for line in open('master_reducer', 'r'):
    data = line.split(",")
    objects.append(data[0])
    performance.append(int(data[1]))
    count += 1
    if count == limit:
        break

#make_cloud(" ".join(objects))

print("Depois >>")

y_pos = np.arange(limit)

plt.bar(y_pos, performance, align='center', alpha=0.2)
plt.xticks(y_pos, objects)
plt.ylabel('Quantidade')
plt.title('Palavras')
plt.show()


