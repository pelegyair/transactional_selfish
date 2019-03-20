#!/usr/bin/python

import queue
import threading
import time
import csv
exitFlag = 0
############################
#!/usr/bin/python3

import random

# selfish mining simulation

# fraction of hash power owned by selfish miner
alpha = 0.25

# fraction of honest miners that build on selfish miner block in a tie.

time_c = 200
iterations = 5000
# check whether the block is mined by the selfish miners.

def isSelfish(alpha):
    return (random.uniform(0, 1) < alpha)

# check whether the miner mines on the selfish chain.
# def isHelper(gamma):
#     return (random.uniform(0, 1) < gamma)
# Goes with seflish

# check whether the miner mines on the selfish chain.

def isNewHelper(smblock,hmblock):
    
    return delta > 0

def avg(lst):
    if len(lst) == 0:
        return current_milli_time()
    return sum(lst)/len(lst)
def runSelfish(iter,q):
    global transactions_num 
    global hmblocks 
    global hmorphans 
    global hmchain 
    global smblocks 
    global smorphans 
    global smchain 
    global transcati 
    global smblock 
    global hmblock
    global exitFlag
    global i
    global time_c
    global gamma
    global new
    global iter_pos
    iLock.acquire()
    while i <= iter:
        print(i)
        if i in iter_pos:
            print(i)
            to_insert = {"index": i,"gamma": -1}
            if new > 0:
                to_insert = {"index": i,"gamma": gamma/new}
            gammas.append(to_insert)
        i += 1
        iLock.release()
        varsLock.acquire()
        
        # Invariants
        # SM chain is always longer than HM chain
        # because otherwise SM switches to HM chain
        assert smchain >= hmchain
        # SM will never risk more than one block to a tie
        assert smchain != hmchain or smchain < 2
        # if (exitFlag == 1):
        #     varsLock.release()
        #     exit(1)
        queueLock.acquire()
        smblock = list(workQueue.queue)
        # print(avg(smblock))
        queueLock.release()
        print("Selfish Mined with " + str(len(smblock)))
        # print(avg(smblock))
        if smchain > 0 and smchain == hmchain:
            # SM publishes its chain to resolve tie.
            smchain = smchain + 1
            smblocks += smchain
            hmorphans += hmchain
            hmchain = 0
            smchain = 0
            # remove transactions
            # queueLock.acquire()
            # workQueue.queue.clear()
            # queueLock.release()
            smblock = []
            hmblock = []
        else:
            # SM mines selfishly
            assert (smchain == 0 and hmchain == 0) or smchain > hmchain
            smchain = smchain + 1
            # TODO: maybe list
        varsLock.release()
        sm = random.expovariate(1.0/SM_AVERAGE_TIME) / time_c
        print("Selfish night for " + str(sm))
        time.sleep(sm)
        print("Good morning Selfish")
        iLock.acquire()
    if iLock.locked():
        iLock.release()


def runHonest(iter,q):
    global transactions_num 
    global hmblocks 
    global hmorphans 
    global hmchain 
    global smblocks 
    global smorphans 
    global smchain 
    global transcati 
    global smblock 
    global hmblock 
    global exitFlag
    global i
    global time_c
    global gamma
    global new
    global iter_pos
    iLock.acquire()
    while i <= iter:
        if i in iter_pos:
            to_insert = {"index": i,"gamma": -1}
            if new > 0:
                to_insert = {"index": i,"gamma": gamma/new}
            gammas.append(to_insert)
        print(i)
        i += 1
        iLock.release()
        #HM found a block
        varsLock.acquire()
        
        queueLock.acquire()
        # while q.full() == False:
        #     queueLock.acquire()
        #     time.sleep(0.001)
        #     queueLock.release()

        hmblock = list(workQueue.queue)
        queueLock.release()
        print("Honest Mined with " + str(len(hmblock)))
        if smchain == 0:
            # HM publishes and SM builds on top               
            assert hmchain == 0
            hmchain = hmchain + 1
            hmblocks += hmchain
            smorphans += smchain
            hmchain = 0
            smchain = 0
            # publish block
            smblock = []
            hmblock = []
            
            # In case of a tie, a fraction of HM may build on SM's chain
            # and this gets the longest published chain
        # elif (smchain == hmchain and isHelper(gamma)):
        delta = avg(smblock) - avg(hmblock)
        new += 1
        if delta > 0:
            gamma +=1
        elif (smchain == hmchain and delta > 0):
            assert hmchain == 1
            smblocks += smchain
            hmorphans += hmchain
            hmchain = 0
            smchain = 0
            hmblocks = hmblocks + 1
            # reset block
            smblock = []
            hmblock = []
        else:
            # HM builds on its own chain.
            hmchain = hmchain + 1
            if smchain == hmchain + 1:
                # If SMs chain is longer by exactly 1,
                # SM will publish his longer chain.
                smblocks += smchain
                hmorphans += hmchain
                hmchain = 0
                smchain = 0
                smblock = []
                hmblock = []

            if hmchain > smchain:
                # if HM has longer chain, SM switches to it.
                hmblocks += hmchain
                smorphans += smchain
                hmchain = 0
                smchain = 0
                smblock = []
                hmblock = []

        queueLock.acquire()
        workQueue.queue.clear()
        queueLock.release()
        varsLock.release()
        hm = random.expovariate(1.0/HM_AVERAGE_TIME) / time_c
        print("Honest night for " + str(hm))
        time.sleep(hm)
        print("Good morning Honest")
        iLock.acquire()
    if iLock.locked():
        iLock.release()

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
    while self.q.full() == False:
        time.sleep(1.75 / time_c)
    print("Starting " + self.name)
    # process_data(self.name, self.q)
    if self.name == "Selfish":
      runSelfish(iterations,self.q)
    elif self.name == "Honest":
      runHonest(iterations,self.q)
    for lock in locks:
        if lock.locked():
            lock.release()
    print("Crying " + self.name)


threadList = ["Selfish","Honest"]
queueLock = threading.Lock()
iLock = threading.Lock()
varsLock = threading.Lock()
locks = [queueLock,iLock,varsLock]
workQueue = queue.Queue(2400)
threadID = 1

threads = []
current_milli_time = lambda: int(round(time.time() * 1000))
#CONSTS
secs = 60
BITCOIN_AVERAGE_TIME = 10*secs

HM_AVERAGE_TIME = BITCOIN_AVERAGE_TIME * 1.0/(1.0-alpha)
SM_AVERAGE_TIME = BITCOIN_AVERAGE_TIME * (1.0/alpha)

transactions_num = 0
hmblocks = 0
hmorphans = 0
hmchain = 0
smblocks = 0
smorphans = 0
smchain = 0
gamma = 0
new = 0
# blocks

transcations = []
smblock = []
hmblock = []
iter_pos = [50,100,250,500,750,1000,1250,1500,1750,2000,2500,3000,4000,5000]
gammas = []
i = 1
# Create new threads
for tname in threadList:
    thread = myThread(threadID, tname, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
sleep_time = 0.15 / time_c
# Fill the queue
try:
    while True:
       queueLock.acquire()
       while workQueue.full() == True:
            queueLock.release()
            workQueue.get()
            # print(workQueue.qsize())
            # time.sleep(sleep_time)
            queueLock.acquire()
       workQueue.put(current_milli_time())
       queueLock.release()
       time.sleep(sleep_time)
       iLock.acquire()
       if i == iterations:
            iLock.release()
            break;
       iLock.release()
except KeyboardInterrupt:
    print('You should\'ve done the LOMDA!')
    exitFlag = 1
    exit(1)
for t in threads:
    t.join()
# Wait for queue to empty
# while not workQueue.empty():
#    pass
# Notify threads it's time to exit
exitFlag = 1
print("Average Selfish block time: " + str(HM_AVERAGE_TIME))
print("Average Honest block time: " + str(SM_AVERAGE_TIME))
print("Iterations: %d, alpha: %f, gamma: %s" % (iterations, alpha, str((gamma/new)) if new > 0 else 'no conflicts'))
print("SM %d blocks, HM %d blocks, ratio %f"
    % (smblocks, hmblocks,
       smblocks / float(smblocks + hmblocks)))
# print("   Orphans: SM %d, HM %d, orphan ratio %f; SM: %f, HM: %f"
#         % (smorphans, hmorphans,
#            (smorphans + hmorphans) / float(smblocks + hmblocks + smorphans + hmorphans),
#            smorphans / float(smblocks + smorphans),
#            hmorphans / float(hmblocks + hmorphans)))
print("still contested: SM %d, HM %d"
        % (smchain, hmchain))
print(iter_pos)
print(gammas)
############################
# Wait for all threads to complete for t in threads:    t.join()
print("Exiting Main Thread")
file = open('results.txt','w')
file.write("Average Selfish block time: " + str(HM_AVERAGE_TIME))
file.write('\n')
file.write("Average Honest block time: " + str(SM_AVERAGE_TIME))
file.write('\n')
file.write("Iterations: %d, alpha: %f, gamma: %s" % (iterations, alpha, str((gamma/new)) if new > 0 else 'no conflicts'))
file.write('\n')
file.write("SM %d blocks, HM %d blocks, ratio %f"
        % (smblocks, hmblocks,
           smblocks / float(smblocks + hmblocks)))
file.write('\n')
# file.write("   Orphans: SM %d, HM %d, orphan ratio %f; SM: %f, HM: %f"
#         % (smorphans, hmorphans,
#            (smorphans + hmorphans) / float(smblocks + hmblocks + smorphans + hmorphans),
#            smorphans / float(smblocks + smorphans),
#            hmorphans / float(hmblocks + hmorphans)))
file.write('\n')
file.write("still contested: SM %d, HM %d"
        % (smchain, hmchain))
file.write(str(iter_pos))
file.write('\n')
file.write(str(gammas))
with open('res.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(iter_pos)
    writer.writerow([p['gamma'] for p in gammas])

