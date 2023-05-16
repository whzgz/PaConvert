import paddle
print('#########################case1#########################')
loss = paddle.nn.BCEWithLogitsLoss(reduction='none')
input = paddle.to_tensor(data=[1.0, 0.7, 0.2], stop_gradient=not True)
target = paddle.to_tensor(data=[1.0, 0.0, 0.0])
output = loss(input, target)
print('#########################case2#########################')
loss = paddle.nn.BCEWithLogitsLoss(weight=paddle.to_tensor(data=[1.0, 0.2, 
    0.2]), reduction='none')
input = paddle.to_tensor(data=[1.0, 0.7, 0.2], stop_gradient=not True)
target = paddle.to_tensor(data=[1.0, 0.0, 0.0])
output = loss(input, target)
print('#########################case3#########################')
loss = paddle.nn.BCEWithLogitsLoss(pos_weight=paddle.ones(shape=[3]))
input = paddle.to_tensor(data=[1.0, 0.7, 0.2], stop_gradient=not True)
target = paddle.to_tensor(data=[1.0, 0.0, 0.0])
output = loss(input, target)
print('#########################case4#########################')
loss = paddle.nn.BCEWithLogitsLoss(reduction='mean')
input = paddle.to_tensor(data=[1.0, 0.7, 0.2], stop_gradient=not True)
target = paddle.to_tensor(data=[1.0, 0.0, 0.0])
output = loss(input, target)
print('#########################case5#########################')
loss = paddle.nn.BCEWithLogitsLoss()
input = paddle.to_tensor(data=[1.0, 0.7, 0.2], stop_gradient=not True)
target = paddle.to_tensor(data=[1.0, 0.0, 0.0])
output = loss(input, target)
