from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original',data_home="./datasets")
print(mnist)