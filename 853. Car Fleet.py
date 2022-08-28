
def carFleet(target, position, speed):
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """
    a = [{'s':speed[i], 'p':position[i], 't': ((target - position[i])/float(speed[i]))} for i in range(len(position)) ]
    a = sorted(a, key= lambda x: x['p'], reverse = True)
    # t = [(target - position[i])/speed[i] for i in range(len(position))]
    st = []
    for i in a:
        if len(st) == 0:
            st.append(i)
        else:
            if i['t'] > st[-1]['t']:
                st.append(i)
    return len(st)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print (carFleet(target, position, speed))