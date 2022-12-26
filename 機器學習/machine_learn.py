from sklearn.datasets import make_blobs


'''
    產生測試資料
    =>  make_blobs(n_samples, n_features, centers, random_state)
`       parameter 如下
        : n_samples: 資料筆數
        : n_features: 變數 / 特徵數量
        : centers: 資料的 分群數量 / 標籤數量
        : random_state: 亂數種子 (指定值，即可確保產生結果一致)
'''

# x 是 特徵(自變數) , y 是標籤 
dx, dy = make_blobs(n_samples=500, n_features=2, centers=2, random_state=0)










