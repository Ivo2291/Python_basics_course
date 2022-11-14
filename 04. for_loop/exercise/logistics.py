goods_count = int(input())

bus = 0
truck = 0
train = 0
tones_price = 0

for goods in range(goods_count):
    tones = int(input())

    if tones <= 3:
        bus += tones
        tones_price += tones * 200
    elif tones <= 11:
        truck += tones
        tones_price += tones * 175
    else:
        train += tones
        tones_price += tones * 120

goods_tones = bus + truck + train
average_price_per_tone = tones_price / goods_tones
bus_percent = bus / goods_tones * 100
truck_percent = truck / goods_tones * 100
train_percent = train / goods_tones * 100

print(f"{average_price_per_tone:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
