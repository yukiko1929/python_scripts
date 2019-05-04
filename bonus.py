# bonus calculation
profits = int(input('how many tens of thousand:'))

if profits > 100:
    bonus = float((profits - 100) * 0.01 + 40 * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1)
elif profits > 60:
    bonus = float((profits - 60) * 0.015 + 20 * 0.03 +  20 * 0.05 + 10 * 0.075 + 10 * 0.1)
elif profits > 40:
    bonus = float((profits - 40) * 0.03 +  20 * 0.05 + 10 * 0.075 + 10 * 0.1)
elif profits > 20:
    bonus = float((profits - 20) * 0.05 + 10 * 0.075 + 10 * 0.1)
elif profits > 10:
    bonus = float('%.2f' % (profits -10) * 0.075 + 10 * 0.1)
else:
    bonus = profits * 0.1

print(bonus)