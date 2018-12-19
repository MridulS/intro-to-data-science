sns.lmplot(x="fare_amount", y="tip_amount",
           data=tips[(tips.fare_amount < 120) & (tips.tip_amount < 30) & (tips.tip_amount > 5) & (tips.fare_amount > 20)],
           hue='off_hour')