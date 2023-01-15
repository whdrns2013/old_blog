---
title: 데이콘 상추 생장률 베이스라인 코드 분석
subtitle: 
author: 
date: 2022-12-13 21:50:06 +0900
lastmod: 2022-12-13 21:50:06 +0900
categories: [Improve,code_analysis]
tags: [코드, 분석, 공부]
pin: false
sitemap :
  changefreq : daily
  priority : 1.0
---
<!--postNo: 20221213_001-->

## 과제 소개


## 베이스라인

### Import

```python
import random
import pandas as pd
import numpy as np
import math
import os
import glob

import tensorflow as tf
from tensorflow.keras.utils import Sequence

from tqdm import tqdm

import warnings
warnings.filterwarnings(action='ignore') 
```

### Hyperparameter Setting

```python
CFG = {
    'EPOCHS':100,
    'LEARNING_RATE':1e-3,
    'BATCH_SIZE':16,
    'SEED':41
}
```

```python
def seed_everything(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

seed_everything(CFG['SEED']) # Seed 고정
```

### Data

```python
all_input_list = sorted(glob.glob('data/train_input/*.csv'))
all_target_list = sorted(glob.glob('data/train_target/*.csv'))

train_input_list = all_input_list[:25]
train_target_list = all_target_list[:25]

val_input_list = all_input_list[25:]
val_target_list = all_target_list[25:]

print(f'학습: {len(train_input_list)}, 검증: {len(val_input_list)}')
```

### Custom Dataset

```python
class Dataloader(tf.keras.utils.Sequence):
    def __init__(self, input_paths, target_paths, batch_size, infer_mode, shuffle=False):
        self.input_paths = input_paths
        self.target_paths = target_paths
        self.batch_size = batch_size
        self.infer_mode = infer_mode
        self.shuffle = shuffle

        self.data_list = []
        self.label_list = []
        print('Data Pre-processing..')
        for input_path, target_path in tqdm(zip(self.input_paths, self.target_paths)):
            input_df = pd.read_csv(input_path)
            target_df = pd.read_csv(target_path)

            input_df = input_df.drop(columns=['obs_time'])
            input_df = input_df.fillna(0)


            target_length = int(len(target_df))

            for idx in range(target_length):
                time_series = input_df[24*idx:24*(idx+1)].values
                self.data_list.append(time_series)

            for label in target_df['predicted_weight_g']:
                self.label_list.append(label)
        print('Done. \n')
        self.on_epoch_end()

    def __len__(self):
        return math.ceil(len(self.data_list)/self.batch_size)

    def __getitem__(self, idx):
        indices = self.indices[idx*self.batch_size:(idx+1)*self.batch_size]

        data = [self.data_list[i] for i in indices]
        label = [self.label_list[i] for i in indices]

        if self.infer_mode == False:
            return tf.convert_to_tensor(data), tf.convert_to_tensor(label)
        else:
            return tf.convert_to_tensor(data)

    def on_epoch_end(self):
        self.indices = np.arange(len(self.data_list))

        if self.shuffle == True:
            np.random.shuffle(self.indices)
```

```python
train_loader = Dataloader(train_input_list, train_target_list, CFG['BATCH_SIZE'], False, shuffle=True)
val_loader = Dataloader(val_input_list, val_target_list, CFG['BATCH_SIZE'], False, shuffle=False)
```


### Model Define

```python
class BaseModel(tf.keras.Model):
    def __init__(self):
        super(BaseModel, self).__init__()
        self.lstm = tf.keras.layers.LSTM(256)
        self.classifier = tf.keras.layers.Dense(1)

    def call(self, inputs):
        h = self.lstm(inputs)
        return self.classifier(h)
```

### Train

```python
model = BaseModel()
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=CFG['LEARNING_RATE']),
    loss=tf.keras.losses.MeanAbsoluteError()
)

model.fit(
    train_loader, validation_data=val_loader, 
    epochs=CFG['EPOCHS'],
    callbacks=[tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, min_lr=1e-8, verbose=1)])
```

### Inference

```python
test_input_list = sorted(glob.glob('data/test_input/*.csv'))
test_target_list = sorted(glob.glob('data/test_target/*.csv'))
```

```python
for test_input_path, test_target_path in zip(test_input_list, test_target_list):
    print(test_target_path)
    test_loader = Dataloader([test_input_path], [test_target_path], CFG['BATCH_SIZE'], True, shuffle=False)
    model_pred = model.predict(test_loader)

    submit_df = pd.read_csv(test_target_path)
    submit_df['predicted_weight_g'] = model_pred
    submit_df.to_csv(test_target_path, index=False)
```