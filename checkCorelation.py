import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import jsonlines

data = [[0,0,0,0,0],[0,0,0,0,0]]
with jsonlines.open('./data/sessions.jsonl') as f:
    for obj in f:
        if obj['event_type'] == 'VIEW_PRODUCT':
            if obj['offered_discount'] == 0:
                data[0][0] += 1
            elif obj['offered_discount'] == 5:
                data[0][1] += 1
            elif obj['offered_discount'] == 10:
                data[0][2] += 1
            elif obj['offered_discount'] == 15:
                data[0][3] += 1
            elif obj['offered_discount'] == 20:
                data[0][4] += 1
        elif obj['event_type'] == 'BUY_PRODUCT':
            if obj['offered_discount'] == 0:
                data[1][0] += 1
            elif obj['offered_discount'] == 5:
                data[1][1] += 1
            elif obj['offered_discount'] == 10:
                data[1][2] += 1
            elif obj['offered_discount'] == 15:
                data[1][3] += 1
            elif obj['offered_discount'] == 20:
                data[1][4] += 1


print("The data to be plotted:\n")
print(data)
labels = ['VIEW_PRODUCT', 'BUY_PRODUCT']
discount = [0, 5, 10, 15, 20]
df_cm = pd.DataFrame(data, index=labels, columns=discount)

# plotting the heatmap
hm = sn.heatmap(data=df_cm, linewidths=.5)

# displaying the plotted heatmap
plt.show()

data = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
with jsonlines.open('./data/sessions.jsonl') as f:
    for obj in f:
        time = obj['timestamp'][:7].replace('-', '')
        if time == '202201':
            if obj['event_type'] == 'VIEW_PRODUCT':
                data[0][0] += 1
            elif obj['event_type'] == 'BUY_PRODUCT':
                data[0][1] += 1
            elif obj['event_type'] == 'RETURN_PRODUCT':
                data[0][2] += 1

        elif time == '202202':
            if obj['event_type'] == 'VIEW_PRODUCT':
                data[1][0] += 1
            elif obj['event_type'] == 'BUY_PRODUCT':
                data[1][1] += 1
            elif obj['event_type'] == 'RETURN_PRODUCT':
                data[1][2] += 1
        elif time == '202203':
            if obj['event_type'] == 'VIEW_PRODUCT':
                data[2][0] += 1
            elif obj['event_type'] == 'BUY_PRODUCT':
                data[2][1] += 1
            elif obj['event_type'] == 'RETURN_PRODUCT':
                data[2][2] += 1
        elif time == '202204':
            if obj['event_type'] == 'VIEW_PRODUCT':
                data[3][0] += 1
            elif obj['event_type'] == 'BUY_PRODUCT':
                data[3][1] += 1
            elif obj['event_type'] == 'RETURN_PRODUCT':
                data[3][2] += 1


print("The data to be plotted:\n")
print(data)
labels = ['January', 'February', 'March', 'April']
event_types = ['VIEW_PRODUCT', 'BUY_PRODUCT', 'RETURN_PRODUCT']
df_cm = pd.DataFrame(data, index=labels, columns=event_types)

# plotting the heatmap
hm = sn.heatmap(data=df_cm, linewidths=.5)

# displaying the plotted heatmap
plt.show()
