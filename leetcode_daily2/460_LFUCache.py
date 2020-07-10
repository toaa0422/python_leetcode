from bisect import bisect_left, insort
#https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html
class LFUCache():  #lfu  least frequently used   区分  least frequent used

    def __init__(self,capacity):

        self.cap,self.tick=capacity,0 # # 容量和计时
        self.his=[] # 元素形式为：(freq, tick, key)   history
        self.dic = {}  # 键值对形式为：key:[val, freq, tick]
    def get(self,key):
        if key not in self.dic:
            return -1
        self.tick+=1
        val,freq,tick=self.dic[key]
        self.dic[key][1]+=1
        self.his.pop(bisect_left(self.his,(freq,tick,key)))
        insort(self.his,(freq+1,self.tick,key))
        return val
    def put(self,key,value):
        if not self.cap:
            return
        self.tick+=1
        if key in self.dic:
            _,freq,tick=self.dic[key]
            self.dic[key[:]]=value,freq+1,self.tick
            self.his.pop(bisect_left(self.his,(freq,tick,key)))
            insort(self.his,(freq+1,self.tick,key))
        else:
            self.dic[key]=[value,1,self.tick]
            if len(self.his)==self.cap:
                del self.dic[self.his.pop(0)[2]]
            insort(self.his,(1,self.tick,key))

from bisect import bisect_left, insort
class LFUCache_:
    def __init__(self, capacity: int):
        self.cap, self.tick = capacity, 0  # 容量和计时
        self.his = []  # 元素形式为：(freq, tick, key)
        self.dic = {}  # 键值对形式为：key:[val, freq, tick]

    def get(self, key: int) -> int:
        if key not in self.dic:  # key不存在
            return -1
        self.tick += 1  # 计时
        val, freq, tick = self.dic[key]  # 取出值、频率和时间
        self.dic[key][1] += 1  # 将频率+1
        self.his.pop(bisect_left(self.his, (freq, tick, key)))  # 找到history里的记录并移除
        insort(self.his, (freq+1, self.tick, key))  # 将更新后的记录二分插入
        return val

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        self.tick += 1
        if key in self.dic:
            _, freq, tick = self.dic[key]  # 取出频率和时间
            self.dic[key][:] = value, freq+1, self.tick  # 更新值、频率和计时
            self.his.pop(bisect_left(self.his, (freq, tick, key)))  # 找到history里的记录并移除
            insort(self.his, (freq+1, self.tick, key))  # 将更新后的记录二分插入
        else:  # 无该记录
            self.dic[key] = [value, 1, self.tick]
            if len(self.his) == self.cap:  # history容量已满
                del self.dic[self.his.pop(0)[2]]  # 移除history首个元素即对应的键值对
            insort(self.his, (1, self.tick, key))  # 将新记录插入history
cache=LFUCache(2)#
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))   # 返回 1
cache.put(3,3)   # 去除 key 2
print(cache.get(2))
print(cache.get(3))      # 返回 3
cache.put(4, 4)   # 去除 key 1
print(cache.get(1))      # 返回 -1 (未找到 key 1)
print(cache.get(3))     # 返回 3
print(cache.get(4))      # 返回 4





"""
缓存算法是指令的一个明细表，用于提示计算设备的缓存信息中哪些条目应该被删去。常见类型包括LFU、LRU、ARC、FIFO、MRU

example:
LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
官方题解 ：  1 哈希表+平衡二叉树 2 双哈希表
"""



