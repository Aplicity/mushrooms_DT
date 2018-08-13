# mushrooms_DT
蘑菇数据集_决策树

## 摘要
  - 介绍了决策树算法的基本原理，给了算法的伪代码，以应届大学生求职为案例逐步解释决策树在属性划分选择、剪纸处理方面上的计算流程。本文介绍了三种属性划分指标的选择，分别为“信息增益”、“增益率”和“基尼指数”。在剪枝处理方面上可以分为预剪枝和后剪枝两张剪枝策略，并都分别给出了案例分析。最后为了更好地说明决策树在分类方面的作用，以kaggle平台上的蘑菇数据集作为学习样本，用python3对数据进行处理分析，最后得出决策树模型图。
  
## 数据集信息  
  - 该数据集包括对应于姬松茸和Lepiota家族中23种蘑菇的假设样品的描述。 每个物种都被确定为绝对可食用，绝对有毒，或具有未知的可食性，不推荐使用。 后一类与有毒类相结合。 “指南”明确指出，确定蘑菇的可食性没有简单的规则; 对于Poisonous Oak和Ivy来说，没有像“传单三，让它成为”的规则。

  - This data set includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family. Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like ``leaflets three, let it be'' for Poisonous Oak and Ivy.
  
## 属性信息
  - cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s 
  - cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s 
  - cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y 
  - bruises?: bruises=t,no=f 
  - odor: almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s 
  - gill-attachment: attached=a,descending=d,free=f,notched=n 
  - gill-spacing: close=c,crowded=w,distant=d 
  - gill-size: broad=b,narrow=n 
  - gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y 
  - stalk-shape: enlarging=e,tapering=t 
  - stalk-root: bulbous=b,club=c,cup=u,equal=e, rhizomorphs=z,rooted=r,missing=? 
  - stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s 
  - stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s 
  - stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y 
  - stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y 
  - veil-type: partial=p,universal=u 
  - veil-color: brown=n,orange=o,white=w,yellow=y 
  - ring-number: none=n,one=o,two=t 
  - ring-type: cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z 
  - spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y 
  - population: abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y 
  - habitat: grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d
  
## 文件说明
  - paper.docx为决策树的理论说明
  - sklearn_DT_mushrooms.py 为引用sklearn库做的决策
  - tree.py、treePlotter.py 为算法代码
  - out.png为模型输出图
![image](https://github.com/Aplicity/mushrooms_DT/blob/master/out.png)
