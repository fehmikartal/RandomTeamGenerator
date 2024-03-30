# RandomTeamGenerator
 RandomTeamGenerator, girdiğiniz listedeki üyeleri seçtiğiniz takım boyutlarına göre gruplandırır.

• **"!fast"** komuduyla seçtiğiniz listedeki isimleri hızlıca iki takıma ayırabilirsiniz.

• **"!drawteam"** komuduyla seçtiğiniz sayıda kişi içeren takımlar oluşturur.

Örnek Input:
```
berkay
ahmet
yusuf
fehmi
eren
fikret
taha
serdar
tutku
utku
arda
```

Örnek Output: (!fast)
```
Team 1: ['arda', 'eren', 'fikret', 'ahmet', 'berkay']
Team 2: ['fehmi', 'tutku', 'serdar', 'utku', 'taha', 'yusuf']
```

Örnek Output: (!drawteam) (Team limit: 3)
```
['tutku', 'yusuf', 'utku']
['ahmet', 'serdar', 'fikret']
['fehmi', 'taha', 'berkay']
['eren', 'arda']
```
