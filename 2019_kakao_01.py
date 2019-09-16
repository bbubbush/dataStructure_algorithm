def solution(record):
    logHistory = [] 
    userStatus = {
        'E' : 'Enter'
        , 'L' : 'Leave'
        , 'C' : 'Change'}   # Can use Status
    userIdDic = {}  # User Id
    splitData = [row.split(' ') for row in record];
    for data in splitData:
        status = data[0]
        userId = data[1]
         # status is 'Leave'
        if status == userStatus['L']:
            log = {
                'userId': userId
                , 'nickName': userIdDic[userId]
            }
            log['msg'] = '님이 나갔습니다.'
            logHistory.append(log)
        # status is 'Enter'
        elif status == userStatus['E']:
            nickName = data[2]
            log = {
                'userId': userId
                , 'nickName': nickName
            }
            userIdDic[userId] = nickName
            log['msg'] = '님이 들어왔습니다.'
            logHistory.append(log)
        # status is 'Change'
        elif status == userStatus['C']:
            nickName = data[2]
            userIdDic[userId] = nickName


    return [(userIdDic.get(log['userId']) + log['msg']) for log in logHistory]


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))