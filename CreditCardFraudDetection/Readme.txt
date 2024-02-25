// Use Dataset Through Kaggle API

1) Download Kaggle.json file From Kaggle Account

```jsx
!mkdir -p ~/.Kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle
```

2) Run the Command

```jsx
// Kaggle API Command
!kaggle datasets download -d mlg-ulb/creditcardfraud
```

3) Unzip the File 

```jsx
from zipfile import ZipFile
dataset = "/content/creditcardfraud.zip"

with ZipFile(dataset, 'r') as zip:
  zip.extractall()
  print("dataset is Extraxted")
```