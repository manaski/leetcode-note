## 思路
主要使用全量搜索的方式进行递归遍历，优化的点在于对于历史记录的保存，减少搜索次数
1. 使用一个整形的位状态保存数字的选择状态
2. 使用缓存保存每个状态下的查找结果，由于搜索具有递归性质，上一次的搜索结果可以被后面递归用到
3. 边界条件的判断

## python3
居然可以定义局部函数，函数标记@cache可以使用内置的缓存机制

## c++
使用map来保存历史结果，c++的数据结构都要include对应的头文件，并且使用std命名空间的
map查找key是否存在，使用count

